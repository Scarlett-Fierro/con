from django.shortcuts import render
from django.db import connection #Trae la conexion de Oracle y nos va a permitir llamar a los Procedimientos Almacenados


# Create your views here.
def home(request):
    data = {
        'personas':listado_personas()
    }

    return render(request, 'core/home.html', data)

def listado_personas():
    django_cursor = connection.cursor()

    #Este es el que llama
    cursor = django_cursor.connection.cursor() #Este cursor nos permitira conectarnos con roacle directamente
    #Este es el que recibe
    out_cur = django_cursor.connection.cursor()  

    cursor.callproc("SP_LISTAR_PERSONAS",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista
