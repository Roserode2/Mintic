'''
 Diseñe un algoritmo que determina si un número es par o impar. 
 Recuerde que un número es par si el resto de una división entera con el número 2 es cero.
'''
#Ejercicio 4
numero = int(input("Ingrese número: "))
def ejercicio_4(numero):
    if numero % 2 == 0:
        return "{0} es par" . format(numero)
    else:
        return "{0} es impar" . format(numero)
print(ejercicio_4(numero)) 