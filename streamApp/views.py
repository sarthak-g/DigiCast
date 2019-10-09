from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")

def trending(request):
    return render(request, "trending.html")

def passbook(request):
    return render(request, "passbook.html")
