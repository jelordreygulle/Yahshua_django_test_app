from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url('', views.post_list, name='post_list'),
]
