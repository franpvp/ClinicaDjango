from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def registro(request):
    return render(request, 'app/registro.html')

def iniciarSesion(request):
    return render(request, 'registration/iniciar-sesion.html')

def modPerfil(request):
    return render(request, 'app/mod-perfil.html')

def userHome(request):
    return render(request, 'app/user-home.html')

def reservarHora(request):
    return render(request, 'app/reservar-hora.html')

def recContraseña(request):
    return render(request, 'app/rec-contraseña.html')

def reclamos(request):
    return render(request, 'app/reclamos.html')


