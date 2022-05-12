'''
Diseñe un algoritmo que permita imprimir un mensaje según la nota definitiva de un estudiante entre 0.0 y 5.0
, de acuerdo conla Tabla:

| nota     | Mensaje a imprimir |
|----------|--------------------|
|  < 3.0   | Insuficiente       |
|  <= 3.5  | Aceptable          |
|  <= 4.0  | Sobresaliente      |
|  <= 5.0  | Excelente          |
'''
nota = float(input("Ingrese nota: "))
def ejercicio_8(nota):
    if nota < 3:
        return "Insuficiente"
    else:
        if nota <= 3.5:
            return "Aceptable"
        else:
            if nota <= 4.0:
                return "Sobresaliente"
            else:
                if nota <= 5.0:
                    return "Excelente"
                else:
                    return "Ingrese calificación válida po' favo'"
print(ejercicio_8(nota))
