# forms.py
from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'titulo', 'tipo', 'data_inicio', 'data_fim', 'valor', 'gratuito',
            'local', 'horario', 'cidade', 'vagas'
        ]
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
            'valor': forms.NumberInput(attrs={'step': '0.01'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        gratuito = cleaned_data.get('gratuito')
        valor = cleaned_data.get('valor')

        if gratuito and valor is not None:
            self.add_error('valor', 'Se a entrada é gratuita, o valor da entrada deve ser deixado em branco.')
        
        if not gratuito and valor is None:
            self.add_error('valor', 'Se a entrada não é gratuita, o valor da entrada deve ser informado.')

        return cleaned_data