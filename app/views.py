from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User, auth
# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
# from django.template.loaders.base import Loader
from django.template.loader import TemplateDoesNotExist, render_to_string
User = get_user_model()


from  django.template import loader
from django.utils.html import strip_tags



def home(request):
    return render(request, "app/d.html")


@login_required(login_url="home")
def p(request):
    stu = Student.objects.all()
    return render(request, "app/gg.html", {"stu": stu})


def reg(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        print("dsnkdkskdsdkskjdksjdjskjdkskjdksjkdjskj", email)
        print("dsnkdkskdsdkskjdksjdjskjdkskjdksjkdjskj", username)

        if password == password2:
            # if User.objects.filter(username=username).exists():
            #     return redirect("reg")

                user = User.objects.create(
                    username=username, password=password, email=email)
                user.save()


                # subject = 'welcome to PPP world'
                # message = f'Hi {user.username}, thank you for registering in PPP.'
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = ["makwanagautam199@gmail.com"]  #user.email,
                # send_mail( subject, message, email_from, recipient_list )
                
                html_content = render_to_string("app/email_template.html",{"title":'test email', 'username': username  })
                text_content = strip_tags(html_content)

                email = EmailMultiAlternatives( 
                'welcome to PPp world',
                text_content,

                # message = f'Hi {text_content}, Thank You For Registering In Python Practical Practice' #{user.username}
                "rajputgautamsinh123@gmail.com",
                # recipient_list = [user.email, ]
                [user.email]
                )
                email.attach_alternative(html_content,"text/html")
                print(email,"dsdskjdkskdjksjkdj")
                email.send()
                print(email,"kskdjskdjksjdksdkjskjjdk")
                # send_mail( subject, message, email_from, recipient_list )
                        # messages.success(request, " Email hasbeen sent successfully...")
                return redirect('login')

        else:
            return redirect("login")




    return render(request,"app/reg.html")


def login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
      

        user = auth.authenticate(username=username,password=password)
              

        if user is not None:
            auth.login(request,user)
            # request.session['is_logged'] = username
            # request.session.set_expiry(200)
            return redirect('home')

       
       

    return render(request,"app/login.html")    



def demo(request):
    return render(request,"app/demo.html")


def email(request):
    return render(request,"app/email_template.html")