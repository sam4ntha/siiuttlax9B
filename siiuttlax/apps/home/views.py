from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def gael(request):
    return render(request, 'gael/gael.html')

def fab(request):
    return render(request,'home/fab.html')

def samantha(request):
    return render(request, 'home/samantha.html')

def fatt(request):
    return render(request, 'home/fatt.html')

def samaria(request):
    return render(request, 'home/samaria.html')  
  
def luis(request):
    return render(request, 'home/luis.html')
