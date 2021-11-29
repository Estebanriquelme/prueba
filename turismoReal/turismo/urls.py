from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('reserva/', reserva, name="reserva"),
    path('inicioSesion/', inicioSesion, name="inicioSesion"),
    path('guardarDatos/', guardarDatos, name="guardarDatos"),

]