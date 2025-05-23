from rest_framework import serializers
from .models import libro, prestamo 
from django.contrib.auth.models import User

class libroSerializer(serializers.ModelSerializer):
    class Meta:
        model = libro
        fields= '__all__'
        
class prestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model= prestamo
        fields = '__all__'
        
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ("first_name", "last_name" ,"username","email", "password","is_staff") #las filas donde se van a guardar la informacion
               
    def create (self, validated_data):
       user= User(**validated_data) #recibe los datos cuando alguien se quiere registar
       user.set_password(validated_data['password'])#luego aca codifica la contraseña ingresada
       user.save()# y la guarda
       return user  