informacion = {
    "id_cliente": 1,
    "nombre": "Ivan",
    "edad": int(input("Ingrese su edad en años: ")),
    "primer_ingreso": True
}


def cliente(informacion: dict):
    nombre = informacion["nombre"]
    edad = informacion["edad"]
    atraccion = ""
    total = ""
    aptitud = True
    pingreso = informacion["primer_ingreso"]
    precio_1 = 10000
    descuento_1 = 0.05
    precio_2 = 5000
    descuento_2 = 0.07
    precio_3 = 20000
    descuento_3 = 0.05
    if informacion["edad"] < 7:
        total = "N/A"  
        atraccion = "N/A"  
        aptitud = False
    else:
        if informacion["edad"] >= 7 and informacion["edad"] < 15 and pingreso == True:
            atraccion = "Sillas voladoras"
            total = precio_1 * (1 - descuento_1)
        else:
            if informacion["edad"] >= 7 and informacion["edad"] < 15 and pingreso != True:
                atraccion = "Sillas voladoras"
                total = precio_1
            else: 
                if informacion["edad"] >= 15 and informacion["edad"] <= 18 and pingreso == True:
                    atraccion = "Carros chocones"
                    total = precio_2 * (1 - descuento_2)
                else:
                    if informacion["edad"] >= 15 and informacion["edad"] <= 18 and pingreso != True:
                        atraccion = "Carros chocones"
                        total = precio_2
                    else:
                        if informacion["edad"] > 18 and pingreso == True:
                            atraccion = "X-Treme"
                            total = precio_3 * (1 - descuento_3)
                        else:
                            if informacion["edad"] > 18 and pingreso != True:
                                atraccion = "X-Treme"
                                total = precio_3                                                                            
    salida = {"nombre": nombre, "edad": edad, "atraccion": atraccion, "apto": aptitud, "primer_ingreso": pingreso, "total_boleta": total}
    return salida
    
print(cliente(informacion))    
        