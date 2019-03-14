from django import forms

from .models import Paitent
from django.utils.safestring import mark_safe


class Signup(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    past_history = forms.CharField( widget=forms.Textarea(attrs={'class': 'container'}) )
    class Meta:
        model = Paitent
        fields = ('name', 'user_name','password','gender','age','past_history')
        
class Login(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Paitent
        fields = ('user_name','password')
        
