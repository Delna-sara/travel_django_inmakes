from django.shortcuts import render
from.models import Places,team_members
# Create your views here.
# static website
def static_website(request):
   obj=Places.objects.all()
   team = team_members.objects.all()

   return render(request,"index.html",{'result':obj,'result1':team})