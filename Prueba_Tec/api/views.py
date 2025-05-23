from django.shortcuts import render
from .serializer import libroSerializer, prestamoSerializer, UsuarioSerializer
from .models import libro, prestamo
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView
from rest_framework import generics

class libroListcreate(generics.ListCreateAPIView):
    queryset = libro.objects.all()
    serializer_class = libroSerializer
    
    
class PrestamoLiscretae(generics.ListCreateAPIView):
    queryset= prestamo.objects.all()
    serializer_class = prestamoSerializer
    permission_classes = [AllowAny]
    
    
    def perform_create(self, serializer):
       libro_obje= serializer.validated_data['libro']
       if not libro_obje.disponible:
           raise ValidationError('El libro no esta disponible')
       
       libro_obje.disponible = False
       libro_obje.save()
       serializer.save(usuario = self.request.user)
       
class UsuarioListCreate(generics.ListCreateAPIView): #Dedfino una vista basada en clases con manejo de metodos, put, delete,post
    queryset= User.objects.all() # Objento el obejto que voy a usar
    serializer_class= UsuarioSerializer #Defino el origen del serializer para covertir el objeto en un formato json
    
    
    def post(self, request, *args, **kwargs): # defino el metodo asociado a la vista
        serializer = self.get_serializer(data=request.data) #Obtengo el serializer asociado a la vista
        if serializer.is_valid(): #Valido 
            serializer.save()# Guardo
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    


