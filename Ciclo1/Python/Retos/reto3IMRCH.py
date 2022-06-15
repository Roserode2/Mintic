# ventas = list()
# def AutoPartes(ventas: list):
#     diccionario = {}
#     for idProducto, dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas:
#         if diccionario.get(idProducto) == None:
#             diccionario[idProducto] = []
#         diccionario[idProducto].append((dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta))
#     return diccionario

# # print(AutoPartes([
# #  (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
# #  (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
# #  (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
# #  (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
# #  (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)

# def consultaRegistro(ventas,idProducto):
#     if idProducto in ventas:
#         for dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador,  fVenta in ventas[idProducto]:
#             print("Producto consultado :", idProducto, " Descripción ", dProducto, " #Parte ", pnProducto, " Cantidad vendida ", cvProducto, " Stock ", sProducto, " Comprador", nComprador, " Documento ", cComprador, " Fecha Venta ", fVenta)
#     else:
#         print("No hay registro de venta de ese producto")

from urllib.parse import _NetlocResultMixinStr


def AutoPartes(ventas: list):
    diccionario = {}
    for x in range(len(ventas)):
        diccionario[x] = [ventas[x]]
    
        
dProducto = None
pnProducto = None
cvProducto = None
sProducto = None
nComprador = None
cComprador = None
fVenta = None

def consultaRegistro(ventas, idProducto):
    diccionarioDos = {}
    for i in ventas:
        if idProducto == ventas [i][0][0]:
            diccionarioDos[i] = ventas[i]
    salida = ""
    if len(diccionarioDos) == 0:
        salida = "No hay registro de venta de ese producto"
    else:
        for i in diccionarioDos:
            salida += "Producto consultado :", idProducto, " Descripción ", dProducto, " #Parte ", pnProducto, " Cantidad vendida ", cvProducto, " Stock ", sProducto, " Comprador", nComprador, " Documento ", cComprador, " Fecha Venta ", fVenta
    print(salida)