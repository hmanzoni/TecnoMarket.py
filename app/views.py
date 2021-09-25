from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm, ProductoForm

# Create your views here.


def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)


def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)


def galeria(request):
    return render(request, 'app/galeria.html')


def agregar_producto(req):
    data = {
        'form': ProductoForm()
    }
    if req.method == 'POST':
        formulario = ProductoForm(data=req.POST, files=req.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(req, 'app/producto/agregar.html', data)


def listar_productos(req):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render(req, 'app/producto/listar.html', data)
