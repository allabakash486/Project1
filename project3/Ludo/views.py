from django.shortcuts import render

# Create your views here.
def Mood(request):
    return render(request,'Basic.html')