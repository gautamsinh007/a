from django.urls  import path
from .import views



urlpatterns = [

    path("h",views.home,name="home"),
    path("p",views.p,name="p"),
    path("",views.login,name="login"),
    path("reg",views.reg,name="reg"),
    path("demo",views.demo,name="demo"),
    path("email",views.email,name="email"),
    
]