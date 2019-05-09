from django.shortcuts import render
# from .forms import *
from django.http import HttpResponse


def te(request):
	return render(request,'index.html')
