from django.shortcuts import render

# Create your views here.

def quienesSomos (request):
    context={}
    return render (request, "quienesSomos/quienesSomos.html")