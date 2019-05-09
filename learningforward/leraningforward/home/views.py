from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .form import *
# from .forms import *
from django.core.exceptions import ValidationError
from django.contrib import messages

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign.html'

# from .form import userform
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog-home.html')


def blogsingle(request):
    return render(request,'blog-single.html')

def coursedetail(request):
    return render(request,'course-details.html')


def courses(request):
    return render(request,'courses.html')

def element(request):
    return render(request,'elements.html')

def eventdetails(request):
    return render(request,'event-details.html')

def events(request):
    return render(request,'events.html')

def gallery(request):
    return render(request,'gallery.html')

def sentmessage(request):
    if request.method == 'GET':
        return render(request,'contact.html',None)
    else:    
        cont =contactme()
        cont.name = request.POST.get('name')
        cont.emailid  = request.POST.get('email')
        cont.subject = request.POST.get('subject')
        cont.messages = request.POST.get('message')
        cont.save()
        messages.success(request, 'message sent successfully!')
        return redirect('/contact/')


def listc(request):
    listing = filec.objects.all()
    data={'listing':listing}
    return render(request,'c.html',data)

def listhtml(request):
    listing = filehtml.objects.all()
    data={'listing':listing}
    return render(request,'htm.html',data)

def listpython(request):
    listing = filepython.objects.all()
    data={'listing':listing}
    return render(request,'python.html',data)


def signup(request):
    if request.method == 'GET':
        obj = tutorform()
        return render(request,'tsignup.html',{'obj':obj})
    else:
        cont =tutor()
        cont.username = request.POST.get('username')
        cont.password  = request.POST.get('password')
        cont.emailid = request.POST.get('emailid')
        cont.phoneno = request.POST.get('phoneno')
        cont.image  = request.POST.get('image')
        cont.address = request.POST.get('address')
        cont.save()
        messages.success(request, 'Signup successfully!')
        return redirect('/tlogin/')

def quiz(request):
    return render(request,'quiz.html')


def tlogin(request):
    if request.method=="GET":
        obj=tutorform()
        data={'obj':obj}
        return render(request,'tlogin.html',data)
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj=tutor.objects.filter(username=username,password=password).first()
        if obj:
            return redirect('/home/')
        else:
            messages.info(request, 'Username is Incorrect!')
            return redirect('/tlogin/')
    
def pythontest(request):
    return render(request,'pythonquiz.html')

def ctest(request):
    return render(request,'ctest.html')
def tutorpage(request):
    return render(request,'tutor.html')