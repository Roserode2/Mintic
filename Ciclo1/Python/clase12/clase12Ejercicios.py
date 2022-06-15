x= int(input("Ingrese número de ejercicio a resolver: "))
if x == 1:
    print("Ingrese una frase y le devolverá la misma sin la palabra 'el'")
    frase = input("Ingrese una frase: ")
    frase = frase.split(" ")
    print(frase)
    lista = [x for x in frase if x != "el"]
    print(lista)
elif x == 2:
    print("Tomará los números de la siguiente lista y filtrará solo los positivos.")
    numeros = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    print(numeros)
    lista = [x for x in numeros if x >= 0]
    print(lista)
elif x == 3:
    print("Extrae los dígitos de una frase y los mete en un conjunto.")
    frase = input("Ingrese frase: ")
    digitos = {x for x in frase}
    print(digitos)
elif x == 4:
    q = int(input("Ingrese valor para usar como base y como exponente: "))
    a = [x**q for x in range(10)]
    b = [q**i for i in range(13)]
    print(a)
    print(b)
elif x == 5:
    print("Se imprimirá el resultado al cubo de los números del 1 al 10.")
    cubo = [x**3 for x in range(11)]
    print(cubo)
elif x == 6:
    frutas = ['mango', 'kiwi', 'fresa', 'guayaba', 'piña', 'mandarina', 'uva', 'banano']
    caracteres = [len(x) for x in frutas]
    print(caracteres)
elif x == 7:
    from prueba import *
    frutas = ['mango', 'kiwi', 'fresa', 'guayaba', 'piña', 'mandarina', 'uva', 'banano']
    vocales = [palabra for palabra in frutas if contar_vocales(palabra) == 2]
    print(vocales)
elif x == 8:
    numero = 1
    primos =[]
    while numero <= 100:
        contador = 1
        x = 0
        while contador <= numero:
            if numero % contador == 0:
                x = x + 1
            contador = contador + 1
        if x == 2:
            primos.append(numero)  
        numero = numero + 1 
    print(primos)
elif x == 9:
    from functools import reduce
    my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
    map_result = list(map(lambda x: round(x**3,3), my_floats )) 
    print(map_result)

    my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
    filter_result = list(filter(lambda name: len(name) <= 7, my_names)) # Arreglar esta instrucción
    print(filter_result)

    my_numbers = [4, 6, 9, 23, 5]
    reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers) # Arreglar esta instrucción
    print(reduce_result)




