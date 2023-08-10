from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# task 1
def home(request):
   return render(request,"home.html")

def about(request):
   return render(request,"about.html")

def contact(request):
   return  HttpResponse("hello i am contact")

def details(request):
   return  HttpResponse("hello i am details")

def thanks(request):
   return  HttpResponse("thank you so much all!!!!")



