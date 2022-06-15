'''
Diseñe un algoritmo que determine mayor número entre cuatro posibles números.
'''
a = float(input("Ingrese primer número: "))
b = float(input("Ingrese segundo número: "))
c = float(input("Ingrese tercer número: "))
d = float(input("Ingrese cuarto número: "))

def ejercicio_9(a, b, c, d):
    if a > b and a > c and a > d:
        return "{0} es mayor que {1}, {2} y {3}" . format(a, b, c, d)
    else:
        if b > c and b > d:
            return "{1} es mayor que {0}, {2} y {3}" . format(a, b, c, d)
        else: 
            if c > d:
                return "{2} es mayor que {0}, {1} y {3}" . format(a, b, c, d)
            else:
                return "{3} es mayor que {0}, {1} y {2}" . format(a, b, c, d)
print(ejercicio_9(a, b, c, d))