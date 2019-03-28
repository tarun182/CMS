"""bms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import index
from compo.views import home, details
from accounts.views import login_view,register_view,logout_view
from compo.views import home
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home),
    path('',index),
    path("accounts/login/", login_view),
    path('accounts/register/', register_view),
    path('accounts/logout/', logout_view),
    #url(r'^details/(?P<Network_ID>\w+)/$', details, name='details'),
    #path('details/<Network_ID>/', details),
    path('<Component_Type>/', details),
    path('MyProducts/', Products)

]
