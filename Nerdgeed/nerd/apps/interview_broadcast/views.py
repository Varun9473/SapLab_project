from django.shortcuts import render,redirect
from .models import Dashbooard
from .form import *
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string, get_template
from django.template import Context
from django.contrib import messages	
from django.http import *
# Create your views here.
def interviewbroadcast(request):
    if request.method == 'GET':
        obj =  dashbordform()
        return render(request,'addcompany.html',{'obj':obj})
    else:
        obj1 = dashbordform(request.POST)
        obj1.save()
        messages.info(request, 'Company Added Successfully')
        return redirect('/display/')





def update(request,id):
    if request.method == 'GET':
        obj1 = Dashbooard.objects.get(id = id)
        form = dashbordform(instance=obj1)
        data = {}
        data ['form'] = form
        return render(request,'update.html',data)
    else:
        obj2 = Dashbooard.objects.get(id = id)
        obj = dashbordform(request.POST,instance=obj2)
        obj.save()
        return redirect('/display/')


def display(request):
    ur = popupuser.objects.all()
    listing = Dashbooard.objects.all()
    if request.method == 'GET':
        un =  popupuserform()
        data={'listing':listing,'un':un}
        return render(request,'list.html',data)
    else:
        obj = popupuserform(request.POST)
        if obj.is_valid():
            name = obj.cleaned_data['name']
            to = obj.cleaned_data['emailid']
            subject = obj.cleaned_data['subject']
            obj.save()
            htmly  = get_template('sendingfile.html')
            data1 = {'listing':listing,'ur':ur}
            html_content = htmly.render(data1)
            try:  
                msg = EmailMultiAlternatives(subject, html_content, settings.EMAIL_HOST_USER, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except:
                return HttpResponse('user is not valid')
    return redirect('/display/')


# def check(request):
#     obj1 = Dashbooard.objects.get(id=id)
#     return render(request,'sendingfile.html',{'obj1':obj1})

def Delete(request, id):
    dsh = Dashbooard.objects.get(id=id)
    dsh.delete()
    return redirect('/display/')

# def mailsend(request,id):
#     obj = dashbooard.objects.get(id = id)
#     form = popupuserform(request.POST)
#     subject = 'my email'
#     msg = get_template('sendingfile.html').render({'obj':obj})
#     to = form.cleaned_data['emailid']
#     res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
#     if res == 1:
#         msg = 'sent'
#     else:
#         msg = 'not sent'
#     return render(request,'sendingfile.html',{'obj':obj})


def mailsend(request,id):
    if request.method == 'GET':
        un =  popupuserform()
        data={'un':un}
        return render(request,'list.html',data)
    else:
        obj = popupuserform(request.POST)
        if obj.is_valid():
            name = obj.cleaned_data['name']
            to = obj.cleaned_data['emailid']
            subject = obj.cleaned_data['subject']
            obj.save()
            try:
                res=send_mail(subject,name,settings.EMAIL_HOST_USER,[to])
            except:
                return HttpResponse('user is not valid')
        return redirect('/display/')



# def popup(request):
#     if request.method == 'GET':
#         un =  popupuserform()
#         return render(request,'list.html',{'un':un})
#     else:
#         obj1 = popupuserform(request.POST)
#         obj1.save()
#         messages.info(request, 'Send Successfully')
#         return redirect('/display/')