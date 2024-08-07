from typing import Any, Dict, Mapping, Optional, Sequence, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.forms.widgets import Widget
from .models import Post

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs) -> None:
        kwargs.setdefault('widget', MultipleFileInput)
        kwargs.setdefault('required',False)
        
        super().__init__(*args, **kwargs)
    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list,tuple)):
            result = [single_file_clean(d,initial) for d in data]
        else:
            result = single_file_clean(data,initial) 
        return result
    

class PostForm(forms.ModelForm):
    images = MultipleFileField()
    class Meta:
        model = Post
        fields = ('title', 'title_kk', 'title_en', 'content', 'content_kk', 'content_en', 'images')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['images'].widget.attrs['id'] = 'file-upload-input'
        self.fields['images'].widget.attrs['onchange'] = 'show_files_name(this)'
        