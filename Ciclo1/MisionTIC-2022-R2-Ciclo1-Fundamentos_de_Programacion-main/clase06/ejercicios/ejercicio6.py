'''
Diseñe un algoritmo que determine si un número real (x)
se encuentra dentro de uno de los siguientes rangos: (3.5, 7.8], [9.3, 4.5) y [23.4, 45.3].
'''
x = float(input("Ingrese número real: "))
def ejercicio_6(x):
    if (x > 3.5  and x < 7.8) or (x < 9.3 and x > 4.5) or (x > 23.4 and x < 45.3):
        return "{} está dentro de uno de los rangos planteados" . format(x)
    else:
        return "{} no está dentro de ninguno de los rangos planteados" . format(x)
print(ejercicio_6(x))