from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def inicio (request):
    context={}
    return render (request, "inicio/index.html", context)

def registrar(request):

    if request.method == "POST":
        usuario=request.POST["usuario"]
        contrasena=request.POST["contrasena"]
        email=request.POST["email"]
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"] 

        user = User.objects.create_user(usuario, email, contrasena)
        user.first_name = nombre
        user.last_name = apellido
        user.save()
        context= {"user": user}
        return render(request, 'inicio/registrarUsuario.html', context)
    else:
        context= {}
        return render(request, 'inicio/registrarUsuario.html', context)