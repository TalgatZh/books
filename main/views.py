from django.shortcuts import render,HttpResponse, render

def books(request):
    return render(request,'books.html')

# Create your views here.
