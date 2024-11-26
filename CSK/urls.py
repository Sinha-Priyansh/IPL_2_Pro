from django.urls import path
from CSK.views import *

urlpatterns=[
    path("Caption/",Caption,name="Caption")


]