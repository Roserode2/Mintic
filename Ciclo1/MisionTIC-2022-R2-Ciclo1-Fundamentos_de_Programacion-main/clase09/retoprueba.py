informacion = {
    "id_cliente": 1,
    "nombre": "Ivan",
    "edad": int(input("Ingrese su edad en años: ")),
    "primer_ingreso": False
}

# def cliente(informacion: dict):
#     newdic = dict()
#     edad = informacion["edad"]
#     apto= True
#     valorboleta=int

#     if edad >18:
#         valorboleta= 20000
#         nombreatraccion="X-Treme"
#         if informacion["primer_ingreso"] == True:
#             valorboleta=valorboleta*0.95

#     else:
#         if edad >=15 and edad<=18:
#             valorboleta=5000
#             nombreatraccion="Carroschocones"
#             if informacion["primer_ingreso"]==True:
#                 valorboleta=valorboleta*0.93
#         else:
#             if edad >=7 and edad <15:
#                 valorboleta=10000
#                 nombreatraccion="Sillas voladoras"
#                 if informacion["primer_ingreso"]== True:
#                     valorboleta=valorboleta*0.95    
#             else:
#                 apto = False
#                 nombreatraccion="N/A"    
#                 valorboleta="N/A"          

#     newdic = {"nombre": informacion["nombre"], "edad": edad, "atraccion": nombreatraccion, "apto": apto, "primer_ingreso": informacion["primer_ingreso"], "total_boleta": valorboleta}
   
#     return newdic

# print(cliente(informacion))

# def cliente (informacion):
#     newdic = dict()
#     edad = informacion["edad"]
#     apto= True
#     valorboleta=int

#     if edad >18:
#         valorboleta= 20000
#         nombreatraccion="X-Treme"
#         if informacion["primer_ingreso"] == True:
#             valorboleta=valorboleta*0.95

#     elif edad >=15 and edad<=18:
#         valorboleta=5000
#         nombreatraccion="Carroschocones"
#         if informacion["primer_ingreso"]==True:
#             valorboleta=valorboleta*0.93
#     elif edad >=7 and edad <15:
#         valorboleta=10000
#         nombreatraccion="Sillas voladoras"
#         if informacion["primer_ingreso"]== True:
#             valorboleta=valorboleta*0.95    
#     else:
#         apto = False
#         nombreatraccion="N/A"    
#         valorboleta="N/A"          


#     newdic["nombre"]= informacion["nombre"]
#     newdic["edad"]= informacion["edad"]
#     newdic["atraccion"]= nombreatraccion
#     newdic["apto"]= apto
#     newdic["primer_ingreso"]= informacion["primer_ingreso"]
#     newdic['total_boleta']= valorboleta
#     return newdic
def cliente (informacion)->dict:
    edad = informacion['edad']
    
    if edad >=18:
        apto=True
        valorboleta= 20000
        atraccion='X-Treme'
        if informacion['primer_ingreso']:
            valorboleta=valorboleta-(valorboleta*0.05)

    elif edad >=15:
        apto=True
        valorboleta=5000
        atraccion='Carros chocones'
        if informacion['primer_ingreso']:
            valorboleta=valorboleta-(valorboleta*0.07)
    elif edad >=7:
        apto=True
        valorboleta=10000
        atraccion='Sillas voladoras'
        if informacion['primer_ingreso']:
            valorboleta=valorboleta-(valorboleta*0.05)
        else:
            atraccion='N/A'
            total_boleta='N/A'
            apto=False


    respuesta={
        'nombre':informacion['nombre'],
        'edad':informacion['edad'],
        'atraccion':atraccion,
        'apto':apto,
        'primer_ingreso':informacion['primer_ingreso'],
        'total_boleta':valorboleta
        
    }
    return respuesta

print(cliente(informacion))