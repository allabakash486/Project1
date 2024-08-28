from django.shortcuts import render

# Create your views here.
def hi(request):
    return render(request,'hi.html')
def student(request):
    return render(request,'student.html')
