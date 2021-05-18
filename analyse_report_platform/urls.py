"""analyse_report_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from app_demo import views as app_demo_views
from django.contrib.auth.decorators import login_required
from django.urls import include
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_demo_views.index, name="index"),
    url(r'^analyse_report/$', app_demo_views.get_analyse_demo, name="demo1"),
    url(r'^demo/$', app_demo_views.get_big_screen, name="demo2"),
    # url(r'^login/$', app_demo_views.login, name="login"),
    # url(r'^login/$', LoginView.as_view, name="login"),
    url(r'^logout/$', app_demo_views.user_logout, name="logout"),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name="login"),
    # url(r'^login_check/$', app_demo_views.login_check, name="login_check"),

]
