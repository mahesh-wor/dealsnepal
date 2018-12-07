from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
    path('',views.homelistview ,name='home_view')
]