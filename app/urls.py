from django.urls import path
from .views import home, registro, iniciarSesion, modPerfil, userHome, reservarHora, recContraseña, reclamos

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('iniciar-sesion/', iniciarSesion, name="iniciar-sesion"),
    path('mod-perfil/', modPerfil, name="mod-perfil"),
    path('user-home/', userHome, name="user-home"),
    path('reservar-hora/',reservarHora,name="reservar-hora"),
    path('rec-contraseña/', recContraseña, name="rec-contraseña"),
    path('reclamos/', reclamos, name="reclamos"),
]