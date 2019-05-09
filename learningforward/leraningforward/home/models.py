from django.db import models
from django.core.validators import FileExtensionValidator
# # Create your models here.
# class register(models.Model):
#     name       = models.CharField(max_length=50)
#     emailid    = models.EmailField()
#     username   = models.CharField(max_length=50,unique=True)
#     password   = models.CharField(max_length=50)
#     mobileno   = models.BigIntegerField(default="")

#     def __str__(self):
#         return self.name

class contactme(models.Model):
    name       = models.CharField(max_length=50)
    emailid    = models.EmailField()
    subject   = models.CharField(max_length=50,unique=True)
    messages   = models.CharField(max_length=500)

class filec(models.Model):
    filename     = models.CharField(max_length=40)
    authorname   = models.CharField(max_length=40,default="")
    fileupload = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf','doc'])])

    def __str__(self):
        return self. filename

class filehtml(models.Model):
    filename     = models.CharField(max_length=40)
    authorname   = models.CharField(max_length=40,default="")
    fileupload = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf','doc'])])

    def __str__(self):
        return self. filename

class filepython(models.Model):
    filename     = models.CharField(max_length=40)
    authorname   = models.CharField(max_length=40,default="")
    fileupload = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf','doc'])])

    def __str__(self):
        return self. filename 

class tutor(models.Model):
    username = models.CharField(max_length=40,unique=True)
    password  = models.CharField(max_length=40)
    emailid   = models.CharField(max_length=40,default="")
    phoneno   = models.BigIntegerField()
    image     = models.ImageField()
    address    = models.CharField(max_length=200)

    def __str__(self):
        return self.username