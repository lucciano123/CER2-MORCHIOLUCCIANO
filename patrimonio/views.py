from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import Categoria, LugarPatrimonial
from .forms import LugarPatrimonialForm

def home(request):
    return render(request, 'patrimonio/home.html')

def catalogo(request):
    categoria_id = request.GET.get('categoria')
    categorias = Categoria.objects.all()
    
    if categoria_id:
        lugares = LugarPatrimonial.objects.filter(categoria_id=categoria_id)
        categoria_seleccionada = get_object_or_404(Categoria, id=categoria_id)
    else:
        lugares = LugarPatrimonial.objects.all()
        categoria_seleccionada = None

    return render(request, 'patrimonio/catalogo.html', {
        'lugares': lugares,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada,
    })

def detalle_lugar(request, pk):
    lugar = get_object_or_404(LugarPatrimonial, pk=pk)
    return render(request, 'patrimonio/detalle.html', {'lugar': lugar})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('catalogo')
    else:
        form = AuthenticationForm()
    return render(request, 'patrimonio/login.html', {'form': form})

# RF09: Cierre de sesión (acepta GET y POST)
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
@permission_required('patrimonio.add_lugarpatrimonial', login_url='sin_permisos')
def crear_lugar(request):
    if request.method == 'POST':
        form = LugarPatrimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = LugarPatrimonialForm()
    return render(request, 'patrimonio/lugar_form.html', {'form': form, 'accion': 'Agregar'})

@login_required
@permission_required('patrimonio.change_lugarpatrimonial', login_url='sin_permisos')
def editar_lugar(request, pk):
    lugar = get_object_or_404(LugarPatrimonial, pk=pk)
    if request.method == 'POST':
        form = LugarPatrimonialForm(request.POST, instance=lugar)
        if form.is_valid():
            form.save()
            return redirect('detalle_lugar', pk=lugar.pk)
    else:
        form = LugarPatrimonialForm(instance=lugar)
    return render(request, 'patrimonio/lugar_form.html', {'form': form, 'accion': 'Editar'})

def sin_permisos(request):
    return render(request, 'patrimonio/sin_permisos.html')