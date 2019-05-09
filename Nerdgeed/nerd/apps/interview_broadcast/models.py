from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class User(models.Model):
    
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50,default="")



# Create your models here.

class Dashbooard(models.Model):
    # jobid               = models.ForeignKey(Job,on_delete=models.CASCADE)
    companyname         = models.CharField(max_length=40)
    position            = models.CharField(max_length=100)
    recruiter           = models.CharField(max_length=40)
    interviewtime       = models.TimeField()
    jobresposibilities  = RichTextField()
    interviewslot       = models.DateTimeField(default="")
    officelocation      = models.CharField(max_length=100)
    signature           = models.CharField(max_length=50)

    def __str__(self):
        return self.companyname

class popupuser(models.Model):
    dashboard       = models.ForeignKey(Dashbooard,on_delete=models.CASCADE,null=True)
    name    = models.CharField(max_length=40)
    emailid = models.EmailField()
    subject = models.CharField(max_length=60)