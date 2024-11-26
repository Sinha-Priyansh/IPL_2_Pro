from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Caption(request):
    return HttpResponse("<h4>Thala for A Reason</h4>")