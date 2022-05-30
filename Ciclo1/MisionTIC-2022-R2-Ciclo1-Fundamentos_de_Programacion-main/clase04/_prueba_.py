import math
from taller import *

x = int(input("Ingrese el numero de ejercicio a realizar 1 a 10: "))

if x == 1:
    nombre = input("Ingrese su nombre: ")
    print(ejercicio_1(nombre))
elif x == 2:
    entero = int(input("Ingrese un entero para calcular su factorial: "))
    print(ejercicio_2(entero))
elif x == 3:
    precio = int(input("Ingrese precio sin impuesto: "))
    iva = input("Ingrese el valor de impuesto en %: ")
    print(ejercicio_3(precio, iva))
elif x == 4:
    radio = int(input("Ingrese radio del circulo en milímetros: "))
    altura = int(input("Ingrese altura del cilindro en milímetros: "))
    def ejercicio_4_b (ejercicio_4_a, altura):
        if altura <= 0:
            return "Ingrese un valor válido de altura."
        else:
            if ejercicio_4_a == type(str):
                return "Ingrese un valor válido de radio."
            else:
                volumen = ejercicio_4_a(radio) * altura
                volumen = round(volumen, 2)
                return volumen
    print("El area del circulo es:", ejercicio_4_a(radio), "milímetros cuadrados")
    print("EL volumen del cilindro es:", ejercicio_4_b((ejercicio_4_a), altura), "milímetros cúbicos")
elif x == 5:
    entero = int(input("Ingrese un número positivo mayor a cero: "))
    print(ejercicio_5(entero))
elif x == 6:
    peso = int(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    print(ejercicio_6(peso, altura))
elif x == 7:
    payasos = int(input("Ingrese números de payasos a enviar: "))
    muñecas = int(input("Ingrese número de muñecas a enviar: ")) 
    print(ejercicio_7(payasos, muñecas))
elif x == 8:
    pan = int(input("Ingrese la cantidad de pan con descuento vendido: "))
    print(ejercicio_8(pan))
elif x == 9:
    dinero = int(input("Ingrese valor a depositar: "))
    print(ejercicio_9(dinero))
elif x == 10:
        segundos = int(input("Ingrese valor de tiempo en segundos: "))
        print(ejercicio_10(segundos))
else:
    print("Ingrese número de ejercicio valido")    
    