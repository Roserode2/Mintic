'''
La oficina de incorporación del ejército necesita un algoritmo que le pueda permitir saber si
un aspirante a ingresar a la institución como soldado es apto o no para poder vincularlo. 
Para que una persona sea apta, debe cumplir los siguientes requisitos:
* Si es mujer, su estatura debe ser superior a 1.60 mts y su edad debe estar entre 20 y 25 años.
* Si el aspirante es hombre, se estatura debe ser superior a 1.65 mts
y su edad debe estar entre los 18 y 24 años.

Tanto mujeres como hombres deben ser solteros. Diseñe el algoritmo de tal forma que permita informar si un aspirante es apto o no para ingresar al ejercito.
'''
genero = input("Ingrese su género (M o F): ")
edad = int(input("Ingrese su edad en años: "))
solt = input("¿Es usted soltero o soltera? (S o N) ")
altura = float(input("Ingrese su estatura en metros: "))

def ejercicio_11(genero: str, edad: int, solt: str, altura: float):
    if genero == "M":
        if solt == "S":
            if edad >= 18 and edad <= 24:
                if altura >= 1.65 and altura <= 2.0:
                    return "El aspirante es apto para incorporarse en el ejército como soldado"
                else:
                    return "El aspirante no es apto para incorporarse en el ejército como soldado"
            else:
                return "El aspirante no es apto para incorporarse en el ejército como soldado"
        else:
            return "El aspirante no es apto para incorporarse en el ejército como soldado"
    elif genero == "F":
        if solt == "S":
            if edad >= 20 and edad <= 25:
                if altura >= 1.60 and altura <= 2.0:
                    return "La aspirante es apta para incorporarse en el ejército como soldado"
                else:
                    return "La aspirante no es apta para incorporarse en el ejército como soldado"
            else:
                return "La aspirante no es apta para incorporarse en el ejército como soldado"
        else:
            return "La aspirante no es apta para incorporarse en el ejército como soldado"
    else:
        return "Ingrese uno de los generos binarios po' favo'"
print(ejercicio_11(genero, edad, solt, altura))
        
                