from django.test import TestCase

from .models import libro


#Bloque de codigo para hacer  testins para los modelos
class libroTestCase(TestCase):
    def setUp(self):
        return libro.objects.create(titulo = "Prueba titulo", autor= "Autor Y", disponible = True)
    
    
    def test_valor_modelo(self):
        objeto = libro.objects.get(titulo= "Prueba titulo")
        self.assertEqual(objeto.autor, "Autor Y")
        self.assertTrue(objeto.disponible)
#--------------------------------------------------------------------------------------


from rest_framework.test import APITestCase
from django.urls import reverse
from .models import libro


#Ejemplo completo de como hacer un testin de models, serializers, vista, Url 
class LibroAPITestCase(APITestCase):

    def setUp(self):
        libro.objects.create(titulo="Django para Todos", autor="Juan Pérez", disponible=True) #Creo un objeto libro con valores iniciales
                                                                                        

    def test_listar_libros(self):
        url = reverse('libro-create') #Se llama el edpoind con la url, aqui lo identifica mediante el nombre que se le dio
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 200) # Verifica que el status sea 200
        self.assertEqual(len(response.data), 1) #Verifica que haya un libro en la respuesta Json
        self.assertEqual(response.data[0]['titulo'], "Django para Todos") #Y verifica que el titulo del libro sea el que ingreso en la posicion 0

    def test_crear_libro(self):
        url = reverse('libro-create') #Envia la peticion Post a la url
        data = {
            "titulo": "Python Avanzado",
            "autor": "Ana Torres",  #Creo el objecto del libro que quiero crear
            "disponible": False
        }
        response = self.client.post(url, data, format='json') 
        self.assertEqual(response.status_code, 201) #Verifica que haya un status 201
        self.assertEqual(libro.objects.count(), 2) #Verifica que hayan 2 libro en la base de datos temporal con el anterio y el nuevo
  
                