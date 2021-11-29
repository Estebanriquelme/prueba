from django.db import models
from django.db.models.aggregates import Min
from django.db.models.deletion import PROTECT
from django.db.models.fields import BooleanField, CharField

# Create your models here.

class Departamento(models.Model):
    id_depto = models.AutoField(primary_key=True)
    pais_depto = models.CharField(max_length=30)
    cuidad_depto = models.CharField(max_length=30)
    direccion_depto = models.CharField(max_length=30)
    nombre_depto = models.CharField(max_length=30)
    n_telefono_depto = models.CharField(max_length=10)
    estado_depto = models.CharField(max_length=15)
    descripcion_depto = models.TextField()
    img_dept = models.ImageField(upload_to ="deptos", null = True)
    precio_depto = models.IntegerField()
    def __str__(self):
        return self.nombre_depto

class Habitacion(models.Model):
    id_habitacion = models.AutoField(primary_key=True)
    numero_hab = models.CharField(max_length=3)
    cantidad_piezas_hab= models.CharField(max_length=2)
    cantidad_bano_hab = models.CharField(max_length=2) 
    metros_cuadrado_hab = models.CharField(max_length=2)
    descripcion_hab = models.TextField()
    departamento = models.ForeignKey(Departamento, on_delete=PROTECT)

    def __str__(self):
        return self.numero_hab

class administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    rut_admin = models.CharField(max_length=10)
    primer_nombre_admin = models.CharField(max_length=30)
    segundo_nombre_admin = models.CharField(max_length=30)
    apellido_paterno_admin = models.CharField(max_length=30)
    apellido_materno_admin = models.CharField(max_length=30)
    correo_admin = models.CharField(max_length=30)
    n_tel_admin = models.CharField(max_length=30)
    sexo_admin = models.CharField(max_length=1)

    def __str__(self):
        return self.primer_nombre_admin
class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    rut_funcionario = models.CharField(max_length=10)
    primer_nombre_funcionario = models.CharField(max_length=30)
    segundo_nombre_funcionario = models.CharField(max_length=30)
    apellido_paterno_funcionario = models.CharField(max_length=30)
    apellido_materno_funcionario = models.CharField(max_length=30)
    correo_funcionario = models.CharField(max_length=30)
    n_tel_funcionario = models.CharField(max_length=30)
    sexo_funcionario = models.CharField(max_length=1)
    depto = models.ForeignKey(Departamento,on_delete=PROTECT)

    def __str__(self):
        return self.primer_nombre_funcionario


class ServicioExtra(models.Model):
    id_serv = models.AutoField(primary_key=True)
    nombre_serv = models.CharField(max_length=15)
    precio_serv = models.IntegerField()

    def __str__(self):
        return self.nombre_serv
class Transporte(models.Model):
    id_trans = models.AutoField(primary_key=True)
    tipo_vehiculo_trans = models.CharField(max_length=15)
    valor_trans = models.IntegerField()
    cantidad_asientos_trans = models.CharField(max_length=2)

    def __str__(self):
        return self.tipo_vehiculo_trans

class Cliente(models.Model):
    rut_cliente = models.CharField( primary_key=True, max_length=10)
    primer_nombre_cliente = models.CharField(max_length=30)
    segundo_nombre_cliente = models.CharField(max_length=30)
    apellido_paterno_cliente = models.CharField(max_length=30)
    apellido_materno_cliente = models.CharField(max_length=30)
    correo_cliente = models.CharField(max_length=30)
    n_tel_cliente = models.CharField(max_length=30)
    sexo_cliente = models.CharField(max_length=1)
    nacionalidad_cliente= models.CharField(max_length=50)
    n_acompanante_cliente= models.IntegerField()

    
    def __str__(self):
        return self.primer_nombre_cliente



class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    estado_reserva = models.CharField(max_length=30)
    costo_reserva = models.IntegerField()
    comentario_reserva= models.CharField(max_length=50)
    cliente = models.CharField(max_length=12)
    trans= models.CharField(max_length=20)
    servicio = models.CharField(max_length=20)
    depto = models.CharField(max_length=20)

    def __str__(self):
        return self.comentario_reserva

class Acompañante(models.Model):
    id_acom = models.AutoField(primary_key=True)
    rut_acom = models.CharField(max_length=10)
    primer_nombre_acom = models.CharField(max_length=30)
    segundo_nombre_acom = models.CharField(max_length=30)
    apellido_paterno_acom = models.CharField(max_length=30)
    apellido_materno_acom = models.CharField(max_length=30)
    correo_acom = models.CharField(max_length=30)
    n_tel_acom = models.CharField(max_length=30)
    sexo_acom = models.CharField(max_length=1)
    cliente = models.ForeignKey(Cliente,on_delete=PROTECT)
    reserva = models.ForeignKey(Reserva, on_delete=PROTECT)
    depto = models.ForeignKey(Departamento,on_delete=PROTECT)

    def __str__(self):
        return self.primer_nombre_acom
    



