from django.shortcuts import render

# Create your views here.

def grocer(request):
    return render(request,'grocer.html')
