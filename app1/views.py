from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new1(request):
    return render(request,'new1.html')
def new2(request):
    return render(request,'new2.html')
def first(request):
    return HttpResponse('this is my first string response in app1')