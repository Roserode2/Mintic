nombre = input("Ingrese su nombre: ")
cantidad = int(input("¿Cuánto dinero ingresará? "))
meses = int(input("¿Por cuántos meses lo ingresará? "))
def CDT(nombre: str, cantidad: int, meses: int):
        porcentaje_interes = 0.03
        porcentaje_a_perder = 0.02       
        if meses > 2:

                vi = ((cantidad * porcentaje_interes * meses)/12)
                vt = vi + cantidad
                salida = "Para el usuario" + nombre + "la cantidad de dinero a recibir, según el monto inicial de" + meses + "meses es:" + vt
                return salida
                                
        else:
                vp = cantidad * porcentaje_a_perder
                vt = cantidad - vp
                return "Para el usuario", nombre, "la cantidad de dinero a recibir, según el monto inicial de", meses, "meses es:", vt
print(CDT(nombre, cantidad, meses))