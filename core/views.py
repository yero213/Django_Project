from django.shortcuts import render

def home(request):
    return render(request, "home.html", {"message": "Welcome to your Django App!"})
# Create your views here.
