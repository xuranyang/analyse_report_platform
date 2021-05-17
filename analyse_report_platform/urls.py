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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_demo_views.index, name="index"),
    url(r'^analyse_report/$', app_demo_views.get_analyse_demo, name="demo1"),
    url(r'^demo/$', app_demo_views.get_big_screen, name="demo2"),
]
