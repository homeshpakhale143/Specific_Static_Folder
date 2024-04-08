from django.shortcuts import render

# Create your views here.

def win(request):
    return render(request,'win.html')
