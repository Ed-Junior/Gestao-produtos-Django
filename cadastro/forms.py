from django.forms import ModelForm
from .models import CadProd

class CadForm(ModelForm):

    class Meta:
        model = CadProd
        fields = ['name', 'classe', 'descricao', 'imagem']