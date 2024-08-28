from django.shortcuts import render

# Create your views here.
def jinja_printing(request):
    d= {'name':'Shaik','age':20,'mob':'63xx299xxxx'}
    return render(request,'jinja_printing.html',d)