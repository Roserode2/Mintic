## Ejercicio 11
'''
Escribir un programa que pida al usuario una palabra
y muestre por pantalla el número de veces que contiene cada vocal.
'''
palabra = input("Ingrese una palabra: ")
lista = [v for v in palabra if v in 'aeiou' or v in 'AEIOU']
vocal = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
for c in vocal:
    veces = 0
    for letra in palabra:
        if letra == vocal:
            veces += 1
        print("La palabra tiene", veces, "veces la letra", c)

print(lista)




    


    