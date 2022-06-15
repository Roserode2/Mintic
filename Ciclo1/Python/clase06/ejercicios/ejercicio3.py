#Diseñe un algoritmo que permita solicitar tanto el nombre como la edad de una persona
#y posteriormente indicar si es “Mayor de edad” o “Menor de edad” según la información ingresada.
#Una persona se considera mayor de edad si tiene 18 años o más.
#Ejercicio_3
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad en años: "))
def ejercicio_3(nombre: str, edad: int):
    if edad >= 18:
        return "{0} es mayor de edad". format(nombre, edad)
    else:
        return "{0} es menor de edad". format(nombre, edad)
print(ejercicio_3(nombre, edad))
