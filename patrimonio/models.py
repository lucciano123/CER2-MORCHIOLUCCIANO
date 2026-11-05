from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class LugarPatrimonial(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    anio_construccion = models.IntegerField(verbose_name="Año de Construcción")
    imagen = models.URLField(help_text="URL de la imagen representativa")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='lugares')

    class Meta:
        verbose_name = "Lugar Patrimonial"
        verbose_name_plural = "Lugares Patrimoniales"

    def __str__(self):
        return self.nombre