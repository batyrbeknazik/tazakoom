from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'news'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.MainPage.as_view(),name='mainPage')
]
