# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

from http.client import responses
import json
from weakref import finalize
import requests
import matplotlib.pyplot as plt


def extraer_info(url):
    response = requests.get(url)
    data = response.json()
    return data

def contar_titulos(datos):
    cant_titulos = {}
    for fila in datos:
        usuario = fila.get('userId')

        if usuario not in cant_titulos and fila.get('completed') == True:
            finalizado = 0
            finalizado += 1
            cant_titulos[usuario] = finalizado
        elif fila.get('completed') == True:
            finalizado += 1
            cant_titulos[usuario] = finalizado

    return cant_titulos

def graficar(cantidad_titulos):
    usuarios = cantidad_titulos.keys()  #guardo en usuarios las keys del diccionario cantidad_titulos
    titulos = cantidad_titulos.values() #guardo en titulos los values del diccionario cantidad_titulos
    
    fig = plt.figure()
    fig.suptitle('Titulos de los Usuarios', fontsize=14)
    ax = fig.add_subplot()

    ax.bar(usuarios, titulos, color='green')
    ax.set_facecolor('whitesmoke')
    ax.set_xlabel('usuarios')
    ax.set_ylabel('titulos')

    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"
    datos = extraer_info(url)
    cantidad_titulos = contar_titulos(datos)
    graficar(cantidad_titulos)

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.
          
    print("terminamos")