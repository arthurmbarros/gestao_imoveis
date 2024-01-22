from django.forms import ModelForm
from django import forms
from appgestaoimoveis.models import Contratos
from appgestaoimoveis.models import Inquilinos
from appgestaoimoveis.models import Imoveis

class InquilinosForm(ModelForm):
    class Meta:
        model = Inquilinos
        fields = ["nome", "documento_tipo", "cpfcnpj", "telefone"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['documento_tipo'].widget.attrs.update({'class': 'mask-documento_tipo'}) 
        self.fields['cpfcnpj'].widget.attrs.update({'class': 'mask-cpfcnpj'})

class ImoveisForm(ModelForm):
    class Meta:
        model = Imoveis
        fields = ["cidade", "endereco"]

class ContratosForm(forms.ModelForm):
    data_base = forms.DateField(
        label='Data',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
            }),
            input_formats=('%Y-%m-%d',),
        )

    class Meta:
        model = Contratos
        fields = ["nome", "endereco", "valor_aluguel", "data_base", "indice"]
