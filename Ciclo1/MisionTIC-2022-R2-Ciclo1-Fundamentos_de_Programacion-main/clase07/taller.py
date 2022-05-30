# Taller Clase 7

## Ejercicio 1
'''Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
'''
def ejercicio_1(numero):
    if numero >= 10 and numero <= 99:
        a = numero // 10
        b = numero % 10
        if a % 2 == 0 and b % 2 == 0:
            return "{0} y {1} son pares." .format(a, b)
        else:
            if a % 2 == 0 and b % 2 != 0:
                return "{0} es par y {1} es impar." .format(a, b)
            else:
                if a % 2 != 0 and b % 2 == 0:
                    return "{0} es impar y {1} es par." .format(a, b)
                else:
                    if a % 2 != 0 and b % 2 != 0:
                        return "{0} y {1} son impares" .format(a, b)
    else:
        return "Ingrese un número de dos dígitos por favor."

## Ejercicio 2
'''
A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora.
Si la cantidad de horas trabajadas es mayor 40 horas. 
La tarifa se incrementa en un 50% para las horas  extras.
Calcular  el  salario  del  trabajador  dadas  las  horas  trabajadas
y  la  tarifa ingresadas por el usuario.
'''
def ejercicio_2(tarifa, horas):
    if tarifa <= 0 or horas <= 0:
        return "Ingrese valores validos requeridos."
    else:
        if horas > 40:
            tarifa = tarifa + (tarifa * 0.5)
            salario = tarifa * horas
            return "El salario del trabajador por trabajar {0} horas es {1:,} COP" .format(horas, salario)
        else:
            salario = tarifa * horas
            return "El salario del trabajador por trabajar {0} horas es {1:,} COP" .format(horas, salario)
        
## Ejercicio 3
'''
Hacer un algoritmo que calcule el total a pagar por la compra de camisas.
Si se compran tres  camisas  o  más  se  aplica  un  descuento  del  20%  sobre  el  total  de  la  compra
y  si  son menos de tres camisas un descuento del 10%
'''
def ejercicio_3(camisas):
    precio = 30000
    desc_1 = (1 - 0.2)
    desc_2 = (1 - 0.1)
    if camisas >= 3:
        precio_final = precio * camisas
        precio_final = precio_final * desc_1
    elif camisas < 3 and camisas > 0:
        precio_final = precio * camisas
        precio_final = precio_final * desc_2
    else:
        return "Ingrese valor valido de camisas."
    return "El valor a pagar es: {}" .format(precio_final)

## Ejercicio 4
'''
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''
def ejercicio_4(nombre, numero):
    if numero >= 1 and numero <= 10:
        return "{}\n" .format(nombre) * numero
    else: 
        return "Ingrese un número entre el 1 al 10."
    
## Ejercicio 5
'''
Escribir un programa que pregunte el nombre del usuario en la consola
y después de que el usuario lo introduzca muestre por pantalla "`<NOMBRE>` tiene `<n>` letras",
donde `<NOMBRE>` es el nombre de usuario en mayúsculas y `<n>` es el número de letras que tienen el nombre.
'''
def ejercicio_5(nombre):
    return "{0} tiene {1} letras." .format(nombre.upper(), len(nombre))
## Ejercicio 6
'''
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
donde el prefijo es el código del país +57, 
y la extensión tiene dos dígitos (por ejemplo +57-313724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato 
y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
'''
def ejercicio_6(telefono):
    return telefono[4:14]

## Ejercicio 7
'''
Hacer un programa que pida al usuario las tres notas de un alumno
(deben estar entre 0 y 5 y pueden tener decimales)
y calcule el promedio e indique mediante un mensaje si aprobó o no (aprueba con nota mayor a 3).
Se debe validar que las notas introducidas estén dentro del rango permitido.
'''
def ejercicio_7(nota_1, nota_2, nota_3):
    if nota_1 >= 0 and nota_1 <= 5 and nota_2 >= 0 and nota_2 <= 5 and nota_3 >= 0 and nota_3 <= 5:
        promedio = (nota_1 + nota_2 + nota_3)/3
        if promedio < 3:
            return "No aprueba."
        else:
            return "Aprueba."
    else:
        return "Alguna de las notas ingresadas no es valida, intente nuevamente."
    
## Ejercicio 8
'''
Crear un algoritmo que indique el valor del descuento de un artículo dependiendo de su valor:

| Rango de valores | Descuento |
|--|--|
| $0 hasta $100.000 | 0% |
|mas de $100.000 hasta $225.000| 1.5% |
|mas de $225.000 hasta $375.000| 3.8% |
|mas de $375.000 | 1.5% |
'''
def ejercicio_8(precio):
    d1 = 1.5
    d2 = 3.8
    d3 = 1.5
    if precio >= 0 and precio <= 100000:
        return "El valor a pagar es {0:,}, no hay descuento disponible." .format(precio)
    else:
        if precio >= 100000 and precio <= 225000:
            desc_1 = (1 - (d1/100))
            des1 = precio * (d1/100)
            precio_final = precio * desc_1
            return "El valor final a pagar es {0:,} con un descuento aplicado de {1} por ciento se descontó {2}" .format(precio_final, d1, des1)
        elif precio > 225000 and precio <= 375000:
            desc_2 = (1 - (d2/100))
            des2 = precio * (d2/100)
            precio_final = precio * desc_2
            return "El valor final a pagar es {0:,} con un descuento aplicado de {1} por ciento se descontó {2}" .format(precio_final, d2, des2)
        elif precio > 375000:
            desc_3 = (1 - (d3/100))
            des3 = precio * (d2/100)
            precio_final = precio * desc_3
            return "El valor final a pagar es {0:,} con un descuento aplicado de {1} por ciento se descontó {2}" .format(precio_final, d3, des3)
        else:
            return "Ingrese un valor de precio valido."
## Ejercicio 9
'''
Crear un algoritmo que permita saber si una ecuación cuadrática tiene o no solución.
Recuerde que una ecuación cuadrática se define como:
![x=\frac{-b\pm\sqrt{b^{2}-4ac} }{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^{2}-4ac}}{2a})
Y se dice que tiene solución si el valor del discriminaste
(que corresponde al cálculo interno de la raíz cuadrada ___b**2−4ac___)
es mayor o igual a cero y el valor de *a* es diferente de cero.
'''
def ejercicio_9(a, b, c):
    if a != 0:
        sq = (b ** 2) - (4*a*c)
        if sq >= 0:
            return "La ecuación sí tiene solución."
        else:
            return "La ecuación no tiene solución."
    else:
        return "La ecuación no tiene solución."
    
## Ejercicio 10
'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato **'dd/mm/aaaa'**
y calcule el dia de la semana que nació.
[Ver el algoritmo aquí](https://www.gaussianos.com/como-calcular-que-dia-de-la-semana-fue/)
'''


