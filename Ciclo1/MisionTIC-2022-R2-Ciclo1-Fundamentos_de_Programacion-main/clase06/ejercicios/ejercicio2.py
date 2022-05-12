#Condicionales
#Ejercicio 2 Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0. 
#El algoritmo debe imprimir el valor ingresado, y un mensaje que indique si el estudiante “Ganó el curso” o “Perdió el curso”. 
# Se gana el curso solo si la nota definitiva es mayor o igual a 3.0.
notaDos = float(input("Ingrese calificación: "))
def ejercicio_2(notaDos):
    if notaDos < 0 or notaDos > 5:
        return "Ingrese calificacion valida"
    elif notaDos >= 3:
        return "Ganó el curso"
    else:
        return "Perdió el curso"
print(ejercicio_2(notaDos))