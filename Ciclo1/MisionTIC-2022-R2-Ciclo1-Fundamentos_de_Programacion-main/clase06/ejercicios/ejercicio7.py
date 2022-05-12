'''
Diseñe un algoritmo que permita imprimir un mensaje según un carácter dado por el usuario, 
independiente que sea ingresado en mayúscula o minúscula, según la Tabla:

| Carácter | Mensaje a imprimir |
|----------|--------------------|
|   'a'    | Android            |
|   'i'    | IOS                |
|   otro   | Opcion inválida    |
'''
car = input("Ingrese caracter: ")
def ejercicio_7(car):
    if car == 'a' or car =='A':
        return "Android"
    elif car == 'i' or car =='I':
            return "IOS"
    else:
        return "Opción inválida"
print(ejercicio_7(car))