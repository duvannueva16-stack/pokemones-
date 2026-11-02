from django.shortcuts import render, get_object_or_404, redirect
from .models import Pokemon, Entrenador, Gimnasio
from .forms import PokemonForm, EntrenadorForm, GimnasioForm
from django.contrib import messages
import random

def lista(request):
    pokemones = Pokemon.objects.all()   # all me trae todos los campos  #}
    buscar = request.GET.get('buscar')

    if buscar:
        pokemones = pokemones.filter(nombre__icontains=buscar)
    return render(request, 'lista.html', {'pokemones': pokemones})

def crear(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pokémon creado correctamente')
            return redirect('pokemon_lista')
    else:
        form = PokemonForm()
    return render(request, 'form.html', {'form': form, 'titulo': 'Nuevo Pokémon'})

def editar(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pokémon editado correctamente')
            return redirect('pokemon_lista')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'form.html', {'form': form, 'titulo': 'Editar Pokémon'})

def eliminar(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == 'POST':
        pokemon.delete()
        messages.success(request, 'Pokémon eliminado')
        return redirect('pokemon_lista')
    return render(request, 'eliminar.html', {'objeto': pokemon})

def entrenador_lista(request):
    entrenadores = Entrenador.objects.all()
    buscar = request.GET.get('buscar')
    if buscar:
        entrenadores = entrenadores.filter(nombre__icontains=buscar)
    return render(request, 'entrenador_lista.html', {'entrenadores': entrenadores})

def entrenador_crear(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entrenador creado correctamente')
            return redirect('entrenador_lista')
    else:
        form = EntrenadorForm()
    return render(request, 'form.html', {'form': form, 'titulo': 'Nuevo Entrenador', 'cancelar': 'entrenador_lista'})



def entrenador_editar(request, id):
    entrenador = get_object_or_404(Entrenador, id=id)
    if request.method == 'POST':
        form = EntrenadorForm(request.POST, instance=entrenador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entrenador editado correctamente')
            return redirect('entrenador_lista')
    else:
        form = EntrenadorForm(instance=entrenador)
    return render(request, 'form.html', {'form': form, 'titulo': 'Editar Entrenador', 'cancelar': 'entrenador_lista'})


def entrenador_eliminar(request, id):
    entrenador = get_object_or_404(Entrenador, id=id)
    if request.method == 'POST':
        entrenador.delete()
        messages.success(request, 'Entrenador eliminado')
        return redirect('entrenador_lista')
    return render(request, 'eliminar.html', {'objeto': entrenador, 'cancelar': 'entrenador_lista'})

def gimnasio_lista(request):
    gimnasios = Gimnasio.objects.all()
    buscar = request.GET.get('buscar')
    if buscar:
        gimnasios = gimnasios.filter(lider__icontains=buscar)
    return render(request, 'gimnasio_lista.html', {'gimnasios': gimnasios})


def gimnasio_crear(request):
    if request.method == 'POST':
        form = GimnasioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gimnasio creado correctamente')
            return redirect('gimnasio_lista')
    else:
        form = GimnasioForm()
    return render(request, 'form.html', {'form': form, 'titulo': 'Nuevo Gimnasio', 'cancelar': 'gimnasio_lista'})


def gimnasio_editar(request, id):
    gimnasio = get_object_or_404(Gimnasio, id=id)
    if request.method == 'POST':
        form = GimnasioForm(request.POST, instance=gimnasio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gimnasio editado correctamente')
            return redirect('gimnasio_lista')
    else:
        form = GimnasioForm(instance=gimnasio)
    return render(request, 'form.html', {'form': form, 'titulo': 'Editar Gimnasio', 'cancelar': 'gimnasio_lista'})


def gimnasio_eliminar(request, id):
    gimnasio = get_object_or_404(Gimnasio, id=id)
    if request.method == 'POST':
        gimnasio.delete()
        messages.success(request, 'Gimnasio eliminado')
        return redirect('gimnasio_lista')
    return render(request, 'eliminar.html', {'objeto': gimnasio, 'cancelar': 'gimnasio_lista'})
    

    