from django import forms
from .models import Reviews, Answer
from django_recaptcha.fields import ReCaptchaField 

class ReviewForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ['author', 'IIN', 'review', 'captcha']
    

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']