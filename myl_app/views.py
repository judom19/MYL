from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,"myl_app/inicio.html")

def catalogo(request):
    return render(request,"myl_app/catalogo.html")

def promociones(request):
    return render(request,"myl_app/promociones.html")

def sucursales(request):
    return render(request,"myl_app/sucursales.html")

def contactanos(request):
    return render(request,"myl_app/contactanos.html")

def ayuda(request):
    return render(request,"myl_app/ayuda.html")

