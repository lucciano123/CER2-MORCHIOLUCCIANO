import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_patrimonio.settings')
django.setup()

from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from patrimonio.models import Categoria, LugarPatrimonial

def cargar_datos():
    print("Iniciando carga de datos de prueba...")

    cat_edificio, _ = Categoria.objects.get_or_create(
        nombre="Edificio Histórico", 
        defaults={"descripcion": "Inmuebles urbanos con valor histórico o arquitectónico."}
    )
    cat_monumento, _ = Categoria.objects.get_or_create(
        nombre="Monumento Nacional", 
        defaults={"descripcion": "Estructuras protegidas por el Estado por su alto valor cultural."}
    )
    cat_mural, _ = Categoria.objects.get_or_create(
        nombre="Mural y Arte Urbano", 
        defaults={"descripcion": "Obras pictóricas en espacios públicos."}
    )

    # 1. Palacio Baburizza (URL funcional)
    lugar1, created1 = LugarPatrimonial.objects.get_or_create(
        nombre="Palacio Baburizza",
        defaults={
            "descripcion": "Hermoso palacio de estilo Art Nouveau ubicado en el cerro Alegre de Valparaíso, actual Museo Municipal de Bellas Artes.",
            "ubicacion": "Paseo Yugoslavo, Cerro Alegre, Valparaíso",
            "anio_construccion": 1916,
            "imagen": "https://images.unsplash.com/photo-1541888946425-d0fbb186a5b3?auto=format&fit=crop&w=800&q=80",
            "categoria": cat_edificio
        }
    )
    if not created1:
        lugar1.imagen = "https://images.unsplash.com/photo-1541888946425-d0fbb186a5b3?auto=format&fit=crop&w=800&q=80"
        lugar1.save()

    # 2. Muelle Vergara (URL funcional)
    lugar2, created2 = LugarPatrimonial.objects.get_or_create(
        nombre="Muelle Vergara",
        defaults={
            "descripcion": "Antiguo muelle industrial recuperado como paseo peatonal e hito turístico en la costa de Viña del Mar.",
            "ubicacion": "Av. San Martín, Viña del Mar",
            "anio_construccion": 1894,
            "imagen": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
            "categoria": cat_monumento
        }
    )
    if not created2:
        lugar2.imagen = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80"
        lugar2.save()

    # 3. Ascensor El Peral (URL funcional)
    lugar3, created3 = LugarPatrimonial.objects.get_or_create(
        nombre="Ascensor El Peral",
        defaults={
            "descripcion": "Típico ascensor funicular que conecta la Plaza Sotomayor con el Paseo Yugoslavo.",
            "ubicacion": "Cerro Alegre, Valparaíso",
            "anio_construccion": 1902,
            "imagen": "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=800&q=80",
            "categoria": cat_monumento
        }
    )
    if not created3:
        lugar3.imagen = "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=800&q=80"
        lugar3.save()

    content_type = ContentType.objects.get_for_model(LugarPatrimonial)
    perm_add = Permission.objects.get(codename='add_lugarpatrimonial', content_type=content_type)
    perm_change = Permission.objects.get(codename='change_lugarpatrimonial', content_type=content_type)

    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@patrimonio.cl", "admin123")
        print("✔ Superusuario creado: admin / admin123")

    if not User.objects.filter(username="editor").exists():
        editor = User.objects.create_user("editor", "editor@patrimonio.cl", "editor123")
        editor.user_permissions.add(perm_add, perm_change)
        print("✔ Usuario Editor creado: editor / editor123 (Permisos de agregar y editar)")

    if not User.objects.filter(username="lector").exists():
        User.objects.create_user("lector", "lector@patrimonio.cl", "lector123")
        print("✔ Usuario Lector creado: lector / lector123 (Sin permisos especiales)")

    print("Carga de datos finalizada con éxito.")

if __name__ == '__main__':
    cargar_datos()