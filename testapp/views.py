from django.shortcuts import render
from django.http import HttpResponse

def greeting(request):
    s="<h1>good morrnig</h1>"
    return HttpResponse(s)
def about(request):
    s="<h1>about page</h1>"
    return HttpResponse(s)
def contact(request):
        s="<h1>contact page</h1>"
        return HttpResponse(s)
