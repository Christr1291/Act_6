from django.contrib import admin
from .models import Proveedor, Producto, Inventario, Direccion, Cliente, Factura

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(Direccion)
admin.site.register(Cliente)
admin.site.register(Factura)
