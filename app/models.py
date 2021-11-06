
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.
from django.contrib.auth.models import PermissionsMixin
from app.managers import BaseAccountManager
from app.managers import *

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=10,primary_key=True)
    email   = models.EmailField(max_length=300)

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff =models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD  = "username"
    REQUIRED_FIELDS = []

    objects = BaseAccountManager()



class Student(models.Model):
    name = models.CharField(max_length=10)
    place = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

