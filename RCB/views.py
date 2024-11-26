from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Caption(request):
    return HttpResponse("<h1><marquee>King Kohli Is The Caption</marquee></h1>")

