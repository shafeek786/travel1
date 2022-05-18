from django.http import HttpResponse
from django.shortcuts import render
from . models import Portfolio
# Create your views here.
def demo(request):
    obj=Portfolio.objects.all()

    return render(request,"index.html",{'result': obj})
def forms(request):
    return render(request,"forms.html")
def about(request):
    return rend
    er(request,"about.html")