from taller import *

x = int(input("Ingrese número de ejercicio a resolver: "))

if x == 1:
    numero = int(input("Ingrese un número de dos dígitos: "))
    print(ejercicio_1(numero))
elif x == 2:
    tarifa = float(input("Ingrese valor a pagar por hora en COP/hora: "))
    horas = int(input("Ingrese horas trabajadas: "))
    print(ejercicio_2(tarifa, horas))
elif x == 3:
    camisas = int(input("Ingrese cantidad de camisas a comprar: "))
    print(ejercicio_3(camisas))    
elif x == 4:
    nombre = input("¿Cuál es su nombre? ")
    numero = int(input("Ingrese un número entre 1 y 10: "))
    print(ejercicio_4(nombre, numero))
elif x == 5:
    nombre = input("¿Cuál es su nombre? ")
    print(ejercicio_5(nombre))
elif x == 6:
    telefono = input("Ingrese teléfono con prefijo y extensión separados por -: ")
    print(ejercicio_6(telefono))
elif x == 7:
    nota_1 = float(input("Ingrese primer nota: "))
    nota_2 = float(input("Ingrese segunda nota: "))
    nota_3 = float(input("Ingrese tercer nota: "))
    print(ejercicio_7(nota_1, nota_2, nota_3))
elif x == 8:
    precio = int(input("Ingrese valor de la compra: "))
    print(ejercicio_8(precio))
elif x == 9:
    a = int(input("Ingrese valor del primer término: "))
    b = int(input("Ingrese valor del segundo término: "))
    c = int(input("Ingrese valor del tercer término: "))
    print(ejercicio_9(a, b, c))
    
    

