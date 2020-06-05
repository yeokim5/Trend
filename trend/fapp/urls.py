"""fapp URL Configuration

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
from fapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.doMessage, name="message"),
    # 빈도수 검색기 폼화면
    path("fapp/message/", views.doMessage, name="message"),
    # ajax가 리퀘스트 URL과 함수
    path("fapp/message2/", views.doMessage2, name="message2"),
    path("fapp/date/", views.doDate, name="date"),
    path("fapp/time/", views.doTime, name="time"),
]