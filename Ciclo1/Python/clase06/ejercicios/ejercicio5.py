'''
Diseñe un algoritmo que determine si un número real (x)
se encuentra dentro del rango abierto-cerrado (3.5, 7.8].
'''
x = float(input("Ingrese número decimal: "))
def ejercicio_5(x):
    if x > 3.5 and x < 7.8:
        return "{0} está dentro del rango" . format(x)
    else:
        return "{0} no está dentro del rango" . format(x)
print(ejercicio_5(x))
    