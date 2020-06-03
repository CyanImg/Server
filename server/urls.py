"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from user import views as user_views
from photographer import views as photographer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/login',user_views.login),
    path('api/user/register',user_views.register),
    path('api/photographer/login',photographer_views.login),
    path('api/photographer/register',photographer_views.register),
    path('api/user/search', user_views.search),
    path('api/user/seticon',user_views.getPic),
    path('api/user/sendcode',user_views.send_forget_code),
    path('api/user/forget',user_views.forget),
    path('api/user/comment',user_views.makeComment),
    path('api/user/order',user_views.makeOrder),
    path('api/user/updateorder',user_views.changeOrder)
]
