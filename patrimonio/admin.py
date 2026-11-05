from django.contrib import admin
from .models import Categoria, LugarPatrimonial

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(LugarPatrimonial)
class LugarPatrimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ubicacion', 'anio_construccion', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'ubicacion')