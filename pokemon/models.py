from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

NATURALEZAS = [
    ('fuego', 'Fuego'),
    ('agua', 'Agua'),
    ('tierra', 'Tierra'),
    ('aire', 'Aire'),
]


class Gimnasio(models.Model):
    lider = models.CharField(max_length=50)
    naturaleza = models.CharField(max_length=50, choices=NATURALEZAS)
    def __str__(self):
        return f"Gimnasio de {self.lider} ({self.naturaleza})"


class Entrenador(models.Model):
    documento = models.BigIntegerField(
    unique=True,
    validators=[MinValueValidator(1000000), MaxValueValidator(999999999999999)])
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    gimnasios = models.ManyToManyField(Gimnasio, blank=True, related_name='entrenadores')
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pokemon(models.Model):
    nombre = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='pokemones/', blank=True, null=True)
    habilidades = models.CharField(max_length=200)
    naturaleza = models.CharField(max_length=50, choices=NATURALEZAS)
    descripcion = models.TextField(blank=True)
    entrenador = models.ForeignKey(
        Entrenador, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='pokemones'
    )

    def __str__(self):
        return self.nombre


