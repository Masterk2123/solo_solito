from django.db import models

# Creando el modelo categoria de de productos.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id categoría")
    
    nombreCategoria = models.CharField(max_length=150, blank=False, null=False, verbose_name="Nombre de la categoría")

    def __str__(self):
        return self.nombreCategoria

# Crando el modelo producto
class Producto(models.Model):
    
    id_producto = models.IntegerField(primary_key=True, verbose_name="id del producto")
    
    producto = models.CharField(max_length=80, blank=False, null=False, verbose_name="nombre del producto")
    
    detalles = models.CharField(max_length=300, null=True, blank=True, verbose_name="detalles del producto")
    
    imagen = models.ImageField(upload_to="images/", default="nn.jpg", null=False, blank=False, verbose_name="Imagen")
    
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.producto
# Create Modelo para vehículo

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name="Patente")
    marca = models.CharField(max_length=80, blank=False, null=False, verbose_name="Marca vehículo")
    modelo = models.CharField(max_length=80, null=True, blank=True, verbose_name="Modelo")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    OPCIONES_SERVICIO = (
        ('suspension_direccion', 'Suspension y Direccion'),
        ('cajas_cambio', 'Cajas de Cambio'),
        ('electronica_automotriz', 'Electronica Automotriz'),
    )
    servicio = models.CharField(max_length=40, blank=False, null=False, verbose_name="servicio", choices=OPCIONES_SERVICIO)
    detalle_servicio = models.CharField(max_length=200, blank=False, null=False, verbose_name="detalle servicio")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.patente

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    technology = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
