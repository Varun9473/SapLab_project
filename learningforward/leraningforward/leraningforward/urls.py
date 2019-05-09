"""leraningforward URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
from home.views import *
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index,name="home"), 
    path('about/',views.about,name="about"),
    path('blog/',views.blog,name="bloghome"),
    path('blogsingle/',views.blogsingle,name="blogsingle"),
    # path('contact/',views.contact,name="contact"),
    path('coursedetails/',views.coursedetail,name="coursedetails"),
    path('courses/',views.courses,name="courses"),
    path('elements/',views.element,name="elements"),
    path('eventdetail/',views.eventdetails,name="eventdetails"),
    path('events/',views.events,name="events"),
    path('gallery/',views.gallery,name="gallery"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('tlogin/',views.tlogin,name="tlogin"),
    # path('', include('home.urls')),
    path('', include('django.contrib.auth.urls')),
    path('contact/',views.sentmessage,name="contact"),
    path('Cfile/',views.listc,name="cfile"),
    path('htmlfile/',views.listhtml,name="htmlfile"),
    path('pythonfile/',views.listpython,name="pythonfile"),
    path('tsignup/',views.signup,name="signupt"),
    path('pythontest/',views.pythontest,name="pythontest"),
    path('ctest/',views.ctest,name="ctest"),
    path('tutorpage/',views.tutorpage,name="tutorpage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)