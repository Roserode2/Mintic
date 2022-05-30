## Ejercicio 10
'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato **'dd/mm/aaaa'**
y calcule el dia de la semana que nació.
[Ver el algoritmo aquí](https://www.gaussianos.com/como-calcular-que-dia-de-la-semana-fue/)
'''
fecha = input("Ingrese día fecha en formato dd/mm/aaaa: ")
siglo = int(fecha[-4:])
sdict = {"0": "5", "1": "3", "2": "1", "3": "0"}
if siglo >= 1700 and siglo <= 1799:
    A = sdict["0"]
elif siglo >= 1800 and siglo <= 1899:
    A = sdict["1"]
elif siglo >= 1900 and siglo <= 1999:
    A = sdict["2"]
elif siglo >= 2000 and siglo <= 2099:
    A = sdict["3"]

año = int(fecha[-2:])




print(siglo, año, A)
    



