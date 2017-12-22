from  django.http import HttpResponse
from django.shortcuts import render
from .models import book

def home(request):
    html="<h1> this is the homepage of your myapp<h1>"
    return HttpResponse(html)

def booklist(request):
    return  render(request,'bookdetails.html',{'book':book.objects.all()})