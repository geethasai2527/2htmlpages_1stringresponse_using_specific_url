from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def new5(request):
    return render(request,'new5.html')
def new6(request):
    return render(request,'new6.html')
def first(request):
    return HttpResponse('this is my first string in app3')