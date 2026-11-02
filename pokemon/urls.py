from django.urls import path
from . import views

urlpatterns = [
    # Pokémon
    path('', views.lista, name='pokemon_lista'),
    path('crear/', views.crear, name='pokemon_crear'),
    path('editar/<int:id>/', views.editar, name='pokemon_editar'),
    path('eliminar/<int:id>/', views.eliminar, name='pokemon_eliminar'),

    # Entrenadores
    path('entrenadores/', views.entrenador_lista, name='entrenador_lista'),
    path('entrenadores/crear/', views.entrenador_crear, name='entrenador_crear'),
    path('entrenadores/editar/<int:id>/', views.entrenador_editar, name='entrenador_editar'),
    path('entrenadores/eliminar/<int:id>/', views.entrenador_eliminar, name='entrenador_eliminar'),

    # Gimnasios
    path('gimnasios/', views.gimnasio_lista, name='gimnasio_lista'),
    path('gimnasios/crear/', views.gimnasio_crear, name='gimnasio_crear'),
    path('gimnasios/editar/<int:id>/', views.gimnasio_editar, name='gimnasio_editar'),
    path('gimnasios/eliminar/<int:id>/', views.gimnasio_eliminar, name='gimnasio_eliminar'),
]