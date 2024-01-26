from django.shortcuts import render

# Create your views here.

def producto (request):
    context={}
    return render (request, "producto/producto.html", context)