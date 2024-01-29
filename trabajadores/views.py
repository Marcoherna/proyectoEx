from django.shortcuts import render
from .models import Trabajador
from .forms import TrabajadorForm

# Create your views here.

def crud(request):
    trabajadores = Trabajador.objects.all()
    context = {'trabajadores':trabajadores}
    return render(request, 'trabajadores/trabajadoresList.html', context)

def trabajadoresAddAdd(request):
    print(request.method)
    rut=request.POST["rut"]
    nombre=request.POST["nombre"]
    aPaterno=request.POST["paterno"]
    aMaterno=request.POST["materno"]
    fechaNac=request.POST["fechaNac"] 
    telefono=request.POST["telefono"]
    email=request.POST["email"]
    direccion=request.POST["direccion"]
    
    obj=Trabajador.objects.create(rut = rut,
                                    nombre = nombre,
                                    apellido_paterno = aPaterno,
                                    apellido_materno = aMaterno,
                                    fecha_nacimiento = fechaNac,
                                    telefono = telefono,
                                    email = email,
                                    direccion = direccion)
    obj.save()
    context = {'mensaje': 'Ok, datos grabados...'}
    return render(request, 'trabajadores/trabajadoresAdd.html', context)


def trabajadores_del(request, pk):
    context={}
    try:
        trabajador = Trabajador.objects.get(rut=pk)
        trabajador .delete()
        mensaje = "Bien, datos eliminados..."
        trabajadores  = Trabajador.objects.all()
        context = {'trabajadores': trabajadores, 'mensaje':mensaje}
        return render(request, 'trabajadores/trabajadoresAdd.html', context)
    except:
        mensaje = "Error, rut no existe..."
        trabajadores  = Trabajador.objects.all()
        context={'trabajadores': trabajadores, 'mensaje':mensaje}
        return render(request, 'trabajadores/trabajadoresAdd.html', context)


def indice(request):
    trabajadores= Trabajador.objects.all()
    form = TrabajadorForm()

   
    
    if request.method == 'POST':
        request.session["email"]="example@example.cl"
        print("por el post")
    else: 
        request.session["email"]="No autenticado"
        print("por el get")
    
    email = request.session["email"]

    context={"trabajadores": trabajadores, 'form': form, 'email':email}


    return render(request, 'trabajadores/indice.html', context)