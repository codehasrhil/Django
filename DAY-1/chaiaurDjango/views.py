from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello world, You are at time pass")
    return render(request,'index.html')

def about(request):
    return HttpResponse("YOu are at harshil rana blog.com for time pass")

def contact(request):
    return HttpResponse("Here is my email you can call me our write email at harshilrana790@gmail.com")