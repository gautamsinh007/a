from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password


class BaseAccountManager(BaseUserManager):
    def create(self,username,password=None,is_superuser=False,**kwargs):
        print("create was code")
        # kwargs.setdefault('is_staff' , is_staff)
        kwargs.setdefault('is_superuser' , is_superuser)
        # kwargs.setdefault('name' , name)
        if  not username:
            raise ValueError('enater valid email address')
        
          
        account = self.model(username=username,**kwargs)
        print("hello ",make_password(password))
        print("passwordd ",password)
        print("passwordddnskdksdjk ",username)
        account.password=make_password(password)

        account.save()

        return account 


      
 

    def create_superuser(self,username, password, **extra_fields):
        print(username)  
    #   extra_fields.setdefault('is_admin' , True)
        extra_fields.setdefault('is_staff' , True)
        extra_fields.setdefault('is_superuser' , True)
        return self.create(username, password, **extra_fields)