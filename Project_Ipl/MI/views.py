from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def Rohit(request):
    return HttpResponse('<h1><marquee>Rohit  is Best  captain in India</marquee></h1>')

def Bumrah(request):
    return render(request,'Bumrah.html')
