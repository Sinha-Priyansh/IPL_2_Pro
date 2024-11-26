from MI.views import *
from django.urls import path

urlpatterns=[
    path("Caption/",Caption,name="Caption"),
]