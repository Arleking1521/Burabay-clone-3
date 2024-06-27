from django import forms
from .models import UserFeedback
from django_recaptcha.fields import ReCaptchaField 

class UserFeedbackForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = UserFeedback
        fields = ['name', 'email', 'message', 'captcha']
