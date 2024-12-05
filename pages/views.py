
from django.shortcuts import render

def about(request):
    return render(request, "pages/about.html")


def home(request):
    return render(request, "pages/home.html")


def contact(request):
    return render(request, "pages/contact.html")
