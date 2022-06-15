# Ejercicios Clase 9

## Ejercicio 1
'''
Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''
def ejercicio_1(entero):
    for i in range(entero, -1, -1):
        if i != 0:
            print(i, end=", ")
        else:
            print(i)
    return "Ese es el conteo regresivo."

## Ejercicio 2
'''
Escribir un programa que pida al usuario un número entero
y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
```
*
**
***
****
***** 
```
'''
def ejercicio_2(entero):
    for i in range(entero):
        print("*"*(i+1))
    return "Se imprimió el triángulo."

## Ejercicio 3
'''
Escribir un programa que pida al usuario un número entero
y muestre por pantalla un triángulo rectángulo como el de más abajo, 
de altura el número introducido.
```
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
```
'''
def ejercicio_3(entero):
    if entero <= 0:
        return "Ingrese número valido."
    else:
        for i in range(1, entero + 1, 2):
            for j in range(i, 0, -2):
                print(j, end=" ")
            print("\t")
    return "Ese es el triángulo que se imprime."

## Ejercicio 4
'''
Escribir un programa que muestre el eco de todo lo que el usuario introduzca
hasta que el usuario escriba “salir” que terminará.
'''
def ejercicio_4(eco):
    while eco != "salir":
        ecoeco = "{} " .format(eco)
        ecoeco = ecoeco * 10
        print(ecoeco)
        eco = input("Ingrese algo: ")
    return "Esos fueron los ecos de las palabras ingresadas."

## Ejercicio 5
'''
Escribir un programa que cree un diccionario de traducción español-inglés. 
El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
y cada par `<palabra>:<traducción>` separados por comas.
El programa debe crear un diccionario con las palabras y sus traducciones.
Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
Si una palabra no está en el diccionario debe dejarla sin traducir.
'''

## Ejercicio 6
'''
Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato:

| Lista de Compra ||
|----|----|
| Articulo 1 | $Precio |
| Articulo 2 | $Precio |
| Articulo 3 | $Precio |
| ... | ... |
| Total | $Costo |
'''
## Ejercicio 7
'''
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista 
y la muestre por pantalla el mensaje **"Yo estudio `<asignatura>`"**, 
donde `<asignatura>` es cada una de las asignaturas de la lista.
'''

## Ejercicio 8
'''
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura
y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''

## Ejercicio 9
'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
'''

## Ejercicio 10
'''
Escribir un programa que almacene en una lista los siguientes precios,
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
'''

## Ejercicio 11
'''
Escribir un programa que pida al usuario una palabra
y muestre por pantalla el número de veces que contiene cada vocal.
'''
## Ejercicio 12
'''
Escribir un programa que reciba una cadena de caracteres
y devuelva un diccionario con cada palabra que contiene y su frecuencia.
Escribir otra función que reciba el diccionario generado con la función anterior
y devuelva una tupla con la palabra más repetida y su frecuencia.
'''