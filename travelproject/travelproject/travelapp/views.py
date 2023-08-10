from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def demo(request):
   return render(request,"ind.html")
def about(request):
   return render(request,"about.html")
def contact(request):
   return  HttpResponse("hello i am contact")

# passing value
def passing_value(request):
   name="india"
   return render(request,"ind.html",{'obj':name})


# passing value from one page to another
def addition(request):
   x=int(request.GET['num1'])
   y = int(request.GET['num2'])
   res=x+y
   return render(request,"addition_result.html",{'result':res})


# static website
def static_website(request):
   return render(request,"index.html")