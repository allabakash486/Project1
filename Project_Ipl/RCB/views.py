from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Virat(request):
    return HttpResponse("<h1><marquee>Virat   is Best  captain in T20's</marquee></h1>")

def Siraj(request):
    return render(request,'Siraj.html')

