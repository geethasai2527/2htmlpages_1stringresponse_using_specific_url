from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new3(request):
    return render(request,'new3.html')
def new4(request):
    return render(request,'new4.html')
def first(request):
    return HttpResponse('this is my first string response in app2')