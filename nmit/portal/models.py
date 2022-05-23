import imp
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Ngo(models.Model):
    ngo_id = models.IntegerField(max_length=100, default=0)
    ngo_name = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=100, null=True)
    mobile_no = models.IntegerField(default=0)

    def __str__(self):
        return self.ngo_name

class Activity(models.Model):
    ngos_activity_id = models.BigIntegerField(max_length=100, default=0)
    activity_id = models.BigIntegerField(max_length=100, default=0)
    activity_name = models.CharField(max_length=50, default="")
    activity_desc = models.CharField(max_length=500)

    def __str__(self):
        return self.activity_name

class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_ngo = models.BooleanField('Is ngo', default=False)
    is_student = models.BooleanField('Is student', default=False)