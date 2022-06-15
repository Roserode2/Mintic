### Ejercicio 7
'''Con la lista `frutas = ['mango', 'kiwi', 'fresa', 'guayaba', 'piña', 'mandarina', 'uva', 'banano']`
generar otra con las frutas que solo tengan exactamente 2 vocales: `['mango', 'kiwi', ...]`.
'''
# def contar_vocales(palabra):
# 	contador = 0
# 	for letra in palabra:
# 		if letra.lower() in "aeiou":
# 			contador += 1
# 	return contador
# # vocales = [x for x in frutas if 'a' or 'e' or 'i' or 'o' or 'u' in x]

# # print(vocales)

### Ejercicio 8 - Especial 
'''Crear una lista con los números primos que existen entre el 2 y el 100.
'''
# x=1
# def conteo(x):
#     for x in range(2,100):
#         x += 1
#     return x
# print(conteo(x))
# numero = 1
# primos =[]
# while numero <= 100:
#     contador = 1
#     x = 0
#     while contador <= numero:
#         if numero % contador == 0:
#             x = x + 1
#         contador = contador + 1
#     if x == 2:
#         primos.append(numero)  
#     numero = numero + 1 
# print(primos)
# def es_primo(num):
#     for n in range(2, 100):
#         if num % n == 0:
#             return False
#     return True
# #primos = [i : for i in range(2, 101)]
# print(es_primo(5))
## Funciones all(), any()
### Ejercicio 10
'''Se recibe una lista de números enteros separados por espacios: Si todos los enteros son positivos,
se debe revisar si algún entero es un número palíndromo como se muestra a continuación 
https://en.wikipedia.org/wiki/Palindromic_number. 
Se imprime la palabra ‘True’ si se cumplen las condiciones o ‘False’ de lo contrario.
Ejemplos:
* Para `[10, 30, 50, 90, 100, 101]` imprime `True`
* Para `[10, 20, 30, 400, 50, 100]` imprime `False`
* Para `[1, 2, 3, 4, 5, 6, 7, 8, 9]` imprime `True`
* Para `[151, 60, -5, 135, 18, 40]` imprime `False`
'''
from functools import reduce
lista = [151, 60, -5, 135, 18, 40]
listring = [str(x) for x in lista]
positivo = all(list(map(lambda x: x > 0, lista)))
pali = list(str(x)[::-1] for x in lista)
ndromo = []
r = bool()
for i in pali:
    for j in listring:
        if i == j:
            r = True
        else:
            r = False
    ndromo.append(r)
if any(ndromo) and positivo:
    print(True)
else: 
    print(False)
# print(pali)
# print(listring)
# print(ndromo)
            

#ndromo = list(x for x in positivo if any([positivo]) == any([positivo][::-1]))
# # print(all(pali))









