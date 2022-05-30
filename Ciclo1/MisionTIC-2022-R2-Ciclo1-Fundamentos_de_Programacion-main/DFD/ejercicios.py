from math import sqrt 
x = int(input("Ingrese numero de ejercicio a resolver: "))

if x == 1:
    libras = float(input("Ingrese peso en libras: "))
    if libras <= 0:
        print("Ingrese valor válido de peso.")
    else:
        kilos = libras / 2
        print("El equivalente es", round(kilos, 2), "kilos")
elif x == 2:
    cateto_1 = float(input("Ingrese cateto 1 en centímetros: "))
    cateto_2 = float(input("Ingrese cateto 2 en centímetros: "))
    if cateto_1 <= 0 or cateto_2 <= 0:
        print("Ingrese valores validos de catetos.")
    else:
        hipotenusa = sqrt(cateto_1 ** 2 + cateto_2 ** 2)
        print("La hipotenusa calculada con estos dos catetos es:", round(hipotenusa, 2), "centímetros")
elif x == 3:
    long = input("¿Qué desea convertir? ¿Millas (mi) o Kilómetros(km)? ")
    if long == "mi":
        mi = float(input("¿Cuánto es la distancia de millas a kilometros a convertir? "))
        km = mi / 0.6213
        print("El equivalente de ", mi, "millas son ", round(km, 2), "kilometros")
    elif long == "km":
        km = float(input("¿Cuánto es la distancia de kilometros a millas a convertir? "))
        mi = km / 1.6093
        print("El equivalente de ", km, "kilometros son ", round(mi, 2), "millas")
    else:
        print("Ingrese una de las 2 opciones 'mi' o 'km'.")
elif x == 4:
    num_1 = float(input("Ingrese un primer número: "))
    num_2 = float(input("Ingrese un segundo número: "))
    
    suma = num_1 + num_2
    resta = num_1 - num_2
    mult = num_1 * num_2
    div = num_1 / num_2
    print("Los resultados de las operaciones con los números ", num_1, " y ", num_2, "son para la suma: ", round(suma, 2), ", para la resta: ", round(resta, 2), "para la multiplicación :" , round(mult, 2), " y para la división: ", round(div, 2))
    
    
    
    