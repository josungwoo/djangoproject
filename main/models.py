from django.db import models

# Create your models here.
class Userinfo(models.Model): # db 새로 만드는 것
    username = models.CharField(max_length=20)
    userid = models.CharField(max_length=20)
    userpw = models.CharField(max_length=20)
    