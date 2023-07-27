from django.urls import path
from app1.views import*
app_name="app1"
urlpatterns=[
    path('new1/',new1,name='new1'),
    path('new2/',new2,name='new2'),
    path('first/',first,name='first'),
]