from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProveedorViewSet, ProductoViewSet, InventarioViewSet, 
    DireccionViewSet, ClienteViewSet, FacturaViewSet,
    TiendaView,
    ProveedorListView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView,
    ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView,
    InventarioListView, InventarioCreateView, InventarioUpdateView, InventarioDeleteView,
    DireccionListView, DireccionCreateView, DireccionUpdateView, DireccionDeleteView,
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    FacturaListView, FacturaCreateView, FacturaUpdateView, FacturaDeleteView, FacturaDetailView
)

# API router
router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'inventarios', InventarioViewSet)
router.register(r'direcciones', DireccionViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'facturas', FacturaViewSet)

# URL patterns for web pages
web_urlpatterns = [
    path('', TiendaView.as_view(), name='tienda-home'),

    # Proveedores
    path('proveedores/', ProveedorListView.as_view(), name='proveedor-list'),
    path('proveedores/nuevo/', ProveedorCreateView.as_view(), name='proveedor-create'),
    path('proveedores/<int:pk>/editar/', ProveedorUpdateView.as_view(), name='proveedor-update'),
    path('proveedores/<int:pk>/eliminar/', ProveedorDeleteView.as_view(), name='proveedor-delete'),

    # Productos
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='producto-create'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto-update'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto-delete'),

    # Inventarios
    path('inventarios/', InventarioListView.as_view(), name='inventario-list'),
    path('inventarios/nuevo/', InventarioCreateView.as_view(), name='inventario-create'),
    path('inventarios/<int:pk>/editar/', InventarioUpdateView.as_view(), name='inventario-update'),
    path('inventarios/<int:pk>/eliminar/', InventarioDeleteView.as_view(), name='inventario-delete'),

    # Direcciones
    path('direcciones/', DireccionListView.as_view(), name='direccion-list'),
    path('direcciones/nueva/', DireccionCreateView.as_view(), name='direccion-create'),
    path('direcciones/<int:pk>/editar/', DireccionUpdateView.as_view(), name='direccion-update'),
    path('direcciones/<int:pk>/eliminar/', DireccionDeleteView.as_view(), name='direccion-delete'),

    # Clientes
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente-delete'),

    # Facturas
    path('facturas/', FacturaListView.as_view(), name='factura-list'),
    path('facturas/nueva/', FacturaCreateView.as_view(), name='factura-create'),
    path('facturas/<int:pk>/', FacturaDetailView.as_view(), name='factura-detail'),
    path('facturas/<int:pk>/editar/', FacturaUpdateView.as_view(), name='factura-update'),
    path('facturas/<int:pk>/eliminar/', FacturaDeleteView.as_view(), name='factura-delete'),
]

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include(web_urlpatterns)),
]
