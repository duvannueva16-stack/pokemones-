from django import forms
from .models import Pokemon, Entrenador, Gimnasio

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'



class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = '__all__'


class GimnasioForm(forms.ModelForm):
    class Meta:
        model = Gimnasio
        fields = '__all__'