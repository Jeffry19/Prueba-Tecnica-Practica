from django.urls import path
from . import views

urlpatterns=[
    
    path('libro/',views.libroListcreate.as_view(), name='Libro-create'),
    path('prestamo/', views.PrestamoLiscretae.as_view(), name='Prestamo'),
    path('user/', views.UsuarioListCreate.as_view(), name='User')
    
]