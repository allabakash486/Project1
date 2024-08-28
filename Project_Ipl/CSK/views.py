from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(request):
    return HttpResponse('<h1><marquee>MSD is cool captain</marquee></h1>')

def jaddu(request):
    return render(request,'jaddu.html')