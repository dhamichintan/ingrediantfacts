from django.http import HttpResponse
from django.shortcuts import render
from djangoproject import product
# Create your views here.
def addproduct(request):
    print("add product called..")
return HttpResponse("addproduct called....")
