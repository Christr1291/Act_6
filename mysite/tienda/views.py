
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Proveedor, Producto, Inventario, Direccion, Cliente, Factura, ItemFactura
from .forms import ClienteForm, DireccionForm, FacturaForm, ItemFacturaFormSet
from rest_framework import viewsets
from .serializers import (
    ProveedorSerializer, ProductoSerializer, InventarioSerializer, 
    DireccionSerializer, ClienteSerializer, FacturaSerializer
)

# API ViewSets
class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

# Template Views
class TiendaView(TemplateView):
    template_name = "tienda/base.html"

# Proveedor Views
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'tienda/proveedor_list.html'

@method_decorator(csrf_exempt, name='dispatch')
class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = '__all__'
    template_name = 'tienda/proveedor_form.html'
    success_url = reverse_lazy('proveedor-list')

@method_decorator(csrf_exempt, name='dispatch')
class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = '__all__'
    template_name = 'tienda/proveedor_form.html'
    success_url = reverse_lazy('proveedor-list')

@method_decorator(csrf_exempt, name='dispatch')
class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'tienda/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor-list')

# Producto Views
class ProductoListView(ListView):
    model = Producto
    template_name = 'tienda/producto_list.html'

@method_decorator(csrf_exempt, name='dispatch')
class ProductoCreateView(CreateView):
    model = Producto
    fields = '__all__'
    template_name = 'tienda/producto_form.html'
    success_url = reverse_lazy('producto-list')

@method_decorator(csrf_exempt, name='dispatch')
class ProductoUpdateView(UpdateView):
    model = Producto
    fields = '__all__'
    template_name = 'tienda/producto_form.html'
    success_url = reverse_lazy('producto-list')

@method_decorator(csrf_exempt, name='dispatch')
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'tienda/producto_confirm_delete.html'
    success_url = reverse_lazy('producto-list')

# Inventario Views
class InventarioListView(ListView):
    model = Inventario
    template_name = 'tienda/inventario_list.html'

@method_decorator(csrf_exempt, name='dispatch')
class InventarioCreateView(CreateView):
    model = Inventario
    fields = '__all__'
    template_name = 'tienda/inventario_form.html'
    success_url = reverse_lazy('inventario-list')

@method_decorator(csrf_exempt, name='dispatch')
class InventarioUpdateView(UpdateView):
    model = Inventario
    fields = '__all__'
    template_name = 'tienda/inventario_form.html'
    success_url = reverse_lazy('inventario-list')

@method_decorator(csrf_exempt, name='dispatch')
class InventarioDeleteView(DeleteView):
    model = Inventario
    template_name = 'tienda/inventario_confirm_delete.html'
    success_url = reverse_lazy('inventario-list')

# Direccion Views
class DireccionListView(ListView):
    model = Direccion
    template_name = 'tienda/direccion_list.html'

@method_decorator(csrf_exempt, name='dispatch')
class DireccionCreateView(CreateView):
    model = Direccion
    form_class = DireccionForm
    template_name = 'tienda/direccion_form.html'
    success_url = reverse_lazy('direccion-list')

@method_decorator(csrf_exempt, name='dispatch')
class DireccionUpdateView(UpdateView):
    model = Direccion
    form_class = DireccionForm
    template_name = 'tienda/direccion_form.html'
    success_url = reverse_lazy('direccion-list')

@method_decorator(csrf_exempt, name='dispatch')
class DireccionDeleteView(DeleteView):
    model = Direccion
    template_name = 'tienda/direccion_confirm_delete.html'
    success_url = reverse_lazy('direccion-list')

# Cliente Views
class ClienteListView(ListView):
    model = Cliente
    template_name = 'tienda/cliente_list.html'

@method_decorator(csrf_exempt, name='dispatch')
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'tienda/cliente_form.html'
    success_url = reverse_lazy('cliente-list')

@method_decorator(csrf_exempt, name='dispatch')
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'tienda/cliente_form.html'
    success_url = reverse_lazy('cliente-list')

@method_decorator(csrf_exempt, name='dispatch')
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'tienda/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')

# Factura Views
class FacturaListView(ListView):
    model = Factura
    template_name = 'tienda/factura_list.html'

class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'tienda/factura_detail.html'

@method_decorator(csrf_exempt, name='dispatch')
class FacturaCreateView(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'tienda/factura_form.html'
    success_url = reverse_lazy('factura-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = ItemFacturaFormSet(self.request.POST)
        else:
            data['items'] = ItemFacturaFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        if items.is_valid():
            self.object = form.save()
            items.instance = self.object
            items.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

@method_decorator(csrf_exempt, name='dispatch')
class FacturaUpdateView(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'tienda/factura_form.html'
    success_url = reverse_lazy('factura-list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = ItemFacturaFormSet(self.request.POST, instance=self.object)
        else:
            data['items'] = ItemFacturaFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        if items.is_valid():
            self.object = form.save()
            items.instance = self.object
            items.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

@method_decorator(csrf_exempt, name='dispatch')
class FacturaDeleteView(DeleteView):
    model = Factura
    template_name = 'tienda/factura_confirm_delete.html'
    success_url = reverse_lazy('factura-list')
