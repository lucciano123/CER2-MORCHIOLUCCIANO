from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('lugar/<int:pk>/', views.detalle_lugar, name='detalle_lugar'),
    path('lugar/nuevo/', views.crear_lugar, name='crear_lugar'),
    path('lugar/<int:pk>/editar/', views.editar_lugar, name='editar_lugar'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('sin-permisos/', views.sin_permisos, name='sin_permisos'),
]