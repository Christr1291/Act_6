from django import forms
from .models import Cliente, Direccion, Factura, ItemFactura

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'correo', 'telefono', 'direccion']

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'ciudad', 'estado', 'codigo_postal', 'pais']

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente', 'fecha']

ItemFacturaFormSet = forms.inlineformset_factory(
    Factura,
    ItemFactura,
    fields=('producto', 'cantidad', 'precio'),
    extra=1,
    can_delete=True
)
