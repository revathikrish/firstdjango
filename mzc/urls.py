from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns=[
    path('',views.indexpage,name='index'),
    path('contacts/',views.contactpage,name='contact'),
    path('home/',views.homepage,name='home')
]