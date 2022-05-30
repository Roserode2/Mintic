tupla = tuple()
tupla = ((
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')), 2010)
#"IdProducto", "dProducto", "pnProducto", "cvProducto", "sProducto", "nComprador", "cComprador", "fVenta"
ventas = [tupla]

def AutoPartes(ventas: list):
    diccionario = {}
    for i in range(len(ventas)):
        diccionario[i] = [ventas[i]]
    return diccionario
'''    
def consultaRegistro(ventas, idProducto):
    resultado2 = {}
    for i in ventas:
        if idProducto == ventas[i][0][0]:
            resultado2[i] = ventas[i] 
    resultado3 = ""
    if len(resultado2) == 0:
        resultado3 = "No hay registro de venta de ese producto\n"
    else:
        for i in resultado2:
            resultado3 += "IdProducto: {}, dProducto: {}, pnProducto: {}, cvProducto: {}, sProducto: {}, nComprador: {}, cComprador: {}, fVenta: {}"
    return print(resultado3)
#return "Producto consultado: {[0][0]} Descripción {[0][1]} #Parte {[0][2]} Cantidad vendida {[0][3]} Stock {[0][4]} Comprador {[0][5]} Documento {[0][6]} Fecha Venta {[0][7]}"  .format(lista, lista, lista, lista, lista, lista, lista, lista)
'''
print(AutoPartes(ventas))
print(type(AutoPartes(ventas)))
