#Condicionales
#Ejercicio 1  Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0.
# El algoritmo debe imprimir el valor ingresado, y de ser una nota mayor o igual a 4.0, deberá imprimir un mensaje de felicitaciones.
nota = float(input("Ingrese calificación: "))
def ejercicio_1(nota):
    if nota < 0 or nota > 5:
        return "Ingrese calificacion valida"
    elif nota >= 4:
        return "{} Felicitaciones!" .format(nota)
    else:
        return nota
print(ejercicio_1(nota))


