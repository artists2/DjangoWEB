"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import notices.views
#from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notices.views._index, name='index'),  # notice/views.py에 있는 index함수 호출 name은 함수를 호출하고 이름을 지정해주는 것
    path('write/', notices.views._write, name='write'),
    path('list/', notices.views._list, name='list'),
    path('introduce/', notices.views._introduce, name='introduce'),
]
