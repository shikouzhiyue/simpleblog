from django.contrib import admin
from django.urls import path
from . import views

# app_name = 'blog'
urlpatterns = ['',
    path(r'^$', views.post_list),
    path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
]
