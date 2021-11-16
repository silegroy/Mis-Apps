from django import forms
from django.forms import ModelForm
from .models import Masaje, Reservas, Masajista
from django.contrib.admin import widgets


# choices = Masaje.objects.get().values_list('duracion_masaje')
# choices_list = []
# for item in choices:
#     choices_list.append(item)

class ReservasForm(forms.ModelForm):
    class Meta:
        
        model = Reservas
        fields = {'habitacion_cliente', 'nombre_cliente', 'fecha_reserva', 'fecha_a_reservar',
                  'hora_reserva', 'quien_realiza', 'nombre_masajista', 'nombre_tratamiento',
                  'duracion_masaje', 'observaciones'}
        
        widgets = {
            
            'habitacion_cliente': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Número de Habitación del Cliente'}),
            'nombre_cliente': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nombre Completo del Cliente'}),
            'fecha_reserva': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'Fecha en la que llega el Cliente a Reservar', 'type':'hidden'}),
            'fecha_a_reservar': forms.DateInput(
                attrs={'class': 'input datepicker', 'placeholder': 'Fecha para la que hará la Reserva'}),
            'hora_reserva': forms.TimeInput(
                attrs={'class': 'form-control', 'placeholder': 'Hora a la que solicita Reservar'}),
            'quien_realiza': forms.TextInput(
                attrs={'class': 'form-control', 'value':'', 'id':'username', 'type':'hidden'}),
            # 'quien_realiza': forms.Select(
            #     attrs={'class': 'form-control', 'placeholder': 'Nombre quien realiza la Reserva'}),
            'nombre_masajista': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Nombre Masajista que lo Atenderá'}),
            'nombre_tratamiento': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Nombre del Tratamiento'}),
            'duracion_masaje': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Tiempo estimado para el Tratamiento'}),
            'observaciones': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Observaciones de la Reserva Realizada'}),
        }
        
       
class TratamientoForm(forms.ModelForm):
    class Meta:
        
        model = Masaje
        fields = {'nombre_tratamiento', 'duracion_masaje'}
        
        widgets = {
            
            'nombre_tratamiento': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Nombre del Tratamiento'}),
            'duracion_masaje': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Duración del Masage en Min, Ej: 50min'}),
            
        }
        
        
class MasajistaForm(forms.ModelForm):
    class Meta:
        
        model = Masajista
        fields = {'nombre_masajista'}
        
        widgets = {            
            'nombre_masajista': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Nombre del Masajista'}),
                        
        }