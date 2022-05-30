import math
## Ejercicio 1
'''Escribir una función a la que se le pase una cadena `<nombre>`
y muestre por pantalla el saludo `¡hola <nombre>!`.
'''
def ejercicio_1(nombre):
        return "Hola! " + nombre

## Ejercicio 2
'''
Escribir una función que reciba un número entero positivo y devuelva su **factorial**.
#entero = int(input("Ingrese un entero: "))
'''

def ejercicio_2(entero):
    if entero < 0:
                return "Ingrese un número positivo"
    else: 
        if (entero == 0):
            return 1
        else: 
            entero = entero * ejercicio_2(entero - 1)
            return entero

#Ejercicio 3
'''
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
y devolver el total de la factura.
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 19%.
'''
def ejercicio_3(precio, iva):
    if iva == "":
        iva = 0.19
        precio_final = precio * (1 - iva)
    else:
        iva = int(iva)
        iva = iva / 100
        precio_final = precio * (1 - iva)
    return "El precio final es: {:.2f}" .format(precio_final)


## Ejercicio 4
'''
Escribir una función que calcule el área de un círculo
y otra que calcule el volumen de un cilindro usando la primera función.
'''

def ejercicio_4_a(radio):
    if radio <= 0:
        return "Ingrese un valor válido del radio."
    else:
        area = math.pi * radio ** 2
        area = round(area, 2)
    return area
    
## Ejercicio 5
'''
Escribir un programa que lea un entero positivo *n*, 
introducido por el usuario y después muestre en pantalla 
la suma de todos los enteros desde 1 hasta *n*. 
La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
![suma = \frac{n(n+1)}{2}](https://latex.codecogs.com/svg.latex?\Large&space;suma=\frac{n(n+1)}{2})
'''

def ejercicio_5(entero):
    if entero > 0:
        suma = ((entero*(entero + 1))/2)
        return "La suma de los números del 1 a {0} es {1}" .format(entero, suma)
    else:
        return "Ingrese número mayor a cero."
    
## Ejercicio 6
'''
Escribir un programa que pida al usuario su peso (en kg)
y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable
y muestre por pantalla la frase `Tu índice de masa corporal es <imc>` donde `<imc>`
es el índice de masa corporal calculado redondeado con dos decimales.
'''
def ejercicio_6(peso, altura):
    if peso > 0 and altura > 0:
        imc = (peso/((altura) ** 2))
        return "Tu índice de masa corporal es : {:.2f}" .format(imc)
    else:
        return "Ingrese valores válidos de peso y altura."

'''
## Ejercicio 7
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido 
y calcule el peso total del paquete que será enviado.
'''

def ejercicio_7(payasos, muñecas):
    if payasos < 0 or muñecas < 0:
        return "Ingrese valor válido del pedido."
    else:
        p_payasos = payasos * 112
        p_muñecas = muñecas * 75
        p_total = p_payasos + p_muñecas
        return "El peso total del pedido es: {} gramos" .format(p_total)

## Ejercicio 8
'''
Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan,
el descuento que se le hace por no ser fresca y el coste final total.
'''
def ejercicio_8(pan):
    if pan > 0:
        precio = 3.49
        precio_normal = pan * precio
        descuento = precio_normal * 0.6
        precio_final = precio_normal - descuento
        return f"Sin descuento el pan costaría {round(precio_normal, 2)} €, pero se descontó {round(descuento, 2)} € y el precio final es {round(precio_final, 2)} €"
    else:
        return "Ingrese valor válido de panes vendidos."


## Ejercicio 9
'''
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
introducida por el usuario. 
Después el programa debe calcular 
y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
Redondear cada cantidad a dos decimales.
'''

def ejercicio_9(dinero):
    if dinero <= 0:
        return "Ingrese valor válido de dinero."
    else:
        año_1 = dinero * 1.04
        año_2 = año_1 * 1.04
        año_3 = año_2 * 1.04
        return f"El valor proyectado a recibir debido a los intereses es {round(año_1, 2)} en el primer año, {round(año_2, 2)} en el segundo año y {round(año_3, 2)} en el tercer año."
    
## Ejercicio 10
'''
Crea un programa que dado un número entero que designa un periodo de tiempo expresado en segundos,
imprima el equivalente en días, horas, minutos y segundos.  
Por ejemplo: 
* 300000 segundos serán 3 días, 11 horas, 20 minutos y 0 segundos.
* 7400 segundos serán 0 días, 2 horas, 3 minutos y 20 segundos.
'''
def ejercicio_10(segundos):
    if segundos < 0:
        return "Ingrese un valor válido de tiempo en segundos."
    else:
        dias = segundos // (24 * 60 * 60)
        seg = segundos % (24 * 60 * 60)
        horas = seg // (60 * 60)
        seg = seg % (60 * 60)
        min = seg // 60
        seg = seg % 60
        return "{0} es equivalente a {1} días, {2} horas, {3} minutos y {4} segundos." .format(segundos, dias, horas, min, seg)