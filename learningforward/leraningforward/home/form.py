from .models import *
from django import forms
from django.forms import ModelForm

# class userform(forms.ModelForm):
#     class Meta:
#         model = register
#         fields  = "__all__"
#         password   = forms.CharField(max_length=50,widget=forms.PasswordInput())
class tutorform(forms.ModelForm):
   """
   A form for creating new tutor. Includes all the required
   fields, plus a repeated password.
   """
   password = forms.CharField(label='Password', widget=forms.PasswordInput)

   class Meta:
       model =  tutor
       fields = '__all__'
      