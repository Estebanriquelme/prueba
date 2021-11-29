from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    deptos = Departamento.objects.all()
    lista = {'deptos':deptos}
    return render(request, 'turismo/home.html', lista)

def reserva(request):
    deptos = Departamento.objects.all()
    serv = ServicioExtra.objects.all() 
    trans = Transporte.objects.all()
    lista = {'deptos':deptos,
            'serv':serv,
            'trans':trans}
    return render(request, 'turismo/reserva.html',lista)

def guardarDatos(request):
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    s_nombre = request.POST['s_nombre']
    ap_pater = request.POST['ap_pater']
    ap_mater = request.POST['ap_mater']
    correo  = request.POST['correo']
    telefono = request.POST['telefono']
    sexo = request.POST['sexo'] 
    pais = request.POST['pais']
    acompañante = request.POST['acompañante'] 
    
    
    cliente = Cliente(rut_cliente=rut,primer_nombre_cliente=nombre,segundo_nombre_cliente=s_nombre,apellido_paterno_cliente=ap_pater,
    apellido_materno_cliente=ap_mater,correo_cliente=correo,n_tel_cliente=telefono,sexo_cliente=sexo,nacionalidad_cliente=pais,n_acompanante_cliente=acompañante)
    cliente.save()
    depto = request.POST['deptos']
    serv = request.POST['servicio']
    trans = request.POST['trans']
    fecha_en = request.POST['fecha_en']
    fecha_sal = request.POST['fecha_en']
    estado = "en curso"
    com = request.POST['comentario']
    reserva =Reserva(fecha_entrada = fecha_en,fecha_salida=fecha_sal,estado_reserva= estado,costo_reserva =50000,comentario_reserva=com, cliente=rut,trans=trans,servicio=serv,depto=depto)
    reserva.save()
    deptos = Departamento.objects.all()
    lista = {'deptos':deptos}
    
    return render(request, 'turismo/home.html',lista)

def inicioSesion(request):
    return render(request, 'turismo/inicioSesion.html')