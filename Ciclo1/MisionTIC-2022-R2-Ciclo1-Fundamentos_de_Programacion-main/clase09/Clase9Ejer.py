from taller import *

x = int(input("Ingrese el número del ejercicio a resolver: "))

if x == 1:
    entero = int(input("Ingrese un número entero positivo para hacer cuenta regresiva: "))
    if entero <= 0:
        print(input("Ingrese número valido.")) 
    else:
        print(ejercicio_1(entero))
elif x == 2:
    entero = int(input("Ingrese un número entero positivo para armar una figura: "))
    if entero <= 0:
        print(input("Ingrese número valido.")) 
    else:
        print(ejercicio_2(entero))
elif x == 3:
    entero = int(input("Ingrese altura del triángulo: "))
    print(ejercicio_3(entero))
elif x == 4:
    eco = input("Ingrese palabra o frase para imprimir eco, escriba \"salir\" para cerrar el ciclo: ")
    print(ejercicio_4(eco))
elif x == 5:
    diccionario = {}
    palabras = input("Ingrese palabras en español:inglés separadas por \":\" : ")
    while palabras != "":
        español, ingles = palabras.split(":")
        diccionario[español] = ingles
        palabras = input("Ingrese palabras en español:inglés separadas por \":\" : ")
    print(diccionario)

    frase = input("Ingrese frase en español para traducir al inglés: ")
    palab = frase.split(" ")
    print(palab)
    for p in palab:
        if p in diccionario:
            print(diccionario[p], end=" ")
        else:
            print(p, end=" ")
elif x == 6:
    cesta = {}
    articulo = input("Ingrese artículo a comprar: ")
    while articulo != "":
        precio = float(input("Ingrese precio del articulo a comprar: "))
        cesta[articulo] = precio
        articulo = input("Ingrese artículo a comprar: ")
    print(cesta)
    cesta = cesta.items()
    print(cesta)
    total = 0
    for articulo, precio in cesta:
        print(articulo, "\t", precio)
        total += precio
    print("Total", "\t", total)
elif x == 7:
    lista = list()
    continuar = True
    while continuar == True:
        asignatura = input("Ingrese una asignatura: ")
        lista += [asignatura]
        continuar = input("¿Desea seguir inscribiendo asignaturas? (Si/No) ") == "Si"
    print("Las asignaturas inscritas son: ", lista)
    for a in lista:
        print("Yo estudio", a)
elif x == 8:
    reporte = ['Programación', 'Inglés', 'Habilidades']
    reprobado = []

    for n in reporte:
        nota = float(input("Ingrese nota definitiva de " + n + " "))
        if nota >= 0 and nota <= 5:
            if nota < 3:
                reprobado.append(n)
        else:
            print("Ingrese valor válido de notas.")
        
    if len(reprobado) >= 1:
        print("Hay que recuperar " + str(reprobado))
    else: 
        print("No hay materias que recuperar.")
elif x == 9:
    palabra = input("Ingrese una palabra para descubrir si es palíndromo: ")
    lista = list()
    alreves = list()
    lista += palabra
    alreves += palabra
    alreves.reverse()
    if lista == alreves:
        print("La palabra", palabra, "es un palíndromo.")
    else:
        print("La palabra", palabra, "no es un palíndromo.")
    print(lista)
    print(alreves)
elif x == 10:
    precios = [50, 75, 46, 22, 80, 65, 8]
    precios.sort()
    print(precios[0], "es el menor y", precios[6], "es el mayor.")
elif x == 11:
    
