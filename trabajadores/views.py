from django.shortcuts import render
from .models import Trabajador
from .forms import TrabajadorForm

# Create your views here.


def crud(request):
    trabajadores = Trabajador.objects.all()
    context = {'trabajadores': trabajadores}
    return render(request, 'trabajadores/trabajadoresList.html', context)


def trabajadoresAdd(request):

    if request.method != "POST":
        context = {}
        return render(request, 'trabajadores/trabajadoresAdd.html', context)
    else:

        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]

        obj = Trabajador.objects.create(rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion)
        obj.save()
        context = {'mensaje': 'Ok, datos grabados...'}
        return render(request, 'trabajadores/trabajadoresAdd.html', context)


def trabajadoresDel(request, pk):
    context = {}
    try:
        trabajadores = Trabajador.objects.get(rut=pk)

        trabajadores.delete()
        mensaje = "Bien, datos eliminados..."
        trabajadores = Trabajador.objects.all()
        context = {'trabajadores': trabajadores, 'mensaje': mensaje}
        return render(request, 'trabajadores/trabajadoresList.html', context)
    except:
        mensaje = "Error, rut no existe..."
        trabajadores = Trabajador.objects.all()
        context = {'trabajadores': trabajadores, 'mensaje': mensaje}
        return render(request, 'trabajadores/trabajadoresList.html', context)


def indice(request):
    trabajadores = Trabajador.objects.all()
    form = TrabajadorForm()

    context = {"trabajadores": trabajadores, 'form': form}

    return render(request, 'trabajadores/indice.html', context)


def trabajadoresFindEdit(request, pk):
    trabajador = Trabajador.objects.get(rut=pk)

    context = {'trabajador': trabajador}

    if trabajador:
        return render(request, 'trabajadores/trabajadoresFindEdit.html', context)
    else:
        context = {'mensaje': "Error, rut no existe..."}
        return render(request, 'trabajadores/trabajadoresList.html', context)


def trabajadoresUpdate(request):
    if request.method == "POST":

        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]

        trabajador = Trabajador()

        trabajador.rut = rut
        trabajador.nombre = nombre
        trabajador.apellido_paterno = aPaterno
        trabajador.apellido_materno = aMaterno
        trabajador.fecha_nacimiento = fechaNac
        trabajador.telefono = telefono
        trabajador.email = email
        trabajador.direccion = direccion

        trabajador.save()

        context = {'trabajador': trabajador}
        return render(request, 'trabajadores/trabajadoresFindEdit.html', context)

    else:
        trabajadores = Trabajador.objects.all()
        context = {'trabajadores': trabajadores}
        return render(request, 'trabajadores/trabajadoresList.html', context)