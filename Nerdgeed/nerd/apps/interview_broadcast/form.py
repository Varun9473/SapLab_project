from django import forms
from django.forms import ModelForm
from .models import *

class dashbordform(forms.ModelForm):
   
    class Meta:
        model = Dashbooard
        fields = '__all__' 

class popupuserform(forms.ModelForm):
   
    class Meta:
        model = popupuser
        fields = '__all__'