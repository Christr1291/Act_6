
from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.CharField(max_length=255)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    nombre_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    stock = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventario de {self.producto.nombre}"

class Direccion(models.Model):
    calle = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20) 
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.calle}, {self.ciudad}, {self.pais}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Factura(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    @property
    def total(self):
        return self.items.aggregate(total=models.Sum(models.F('cantidad') * models.F('precio')))['total'] or 0

    def __str__(self):
        return f"Factura {self.id} - {self.cliente}"

class ItemFactura(models.Model):
    factura = models.ForeignKey(Factura, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_item(self):
        return self.cantidad * self.precio

    def __str__(self):
        return f"{self.producto.nombre} ({self.cantidad})"
