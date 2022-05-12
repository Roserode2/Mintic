'''
La oficina de aguas de la ciudad requiere crear un algoritmo que le permita liquidar las facturas de sus clientes durante cada mes.
El cobro de cada factura se realiza de la siguiente forma: 
se cobra el cargo fijo, el consumo de agua en el periodo, es decir, la cantidad de metros consumidos
y el servicio de recolección de basuras y alcantarillado.
Construya un algoritmo que, al ingresarle es estrato socioeconomico del predio
y la cantidad de metros cúbicos de agua consumidos, permita determinar el valor de la factura a pagar. 
Todos estos cobros se llevan a cabo dependiendo del estrato socioeconómico al que pertenezca el predio, 
de acuerdo con la siguiente tabla:

|Estrato|Cargo Fijo|Metro3 consumido|Basuras y alcantarillado|
|-------|-----|-----|------|
|1      |$2500|$2200|$5500 |
|2      |$2800|$2350|$6200 |
|3      |$3000|$2600|$7400 |
|4      |$3300|$3400|$8600 |
|5      |$3700|$3900|$9700 |
|6      |$4400|$4800|$11000|
'''
estrato = int(input("Ingrese el estrato del predio: "))
mc = float(input("Ingrese el metro cubico consumido al mes: "))

def ejercicio_10(estrato: int, mc: float):
    if estrato == 1:
        pt = 2500 + mc * 2200 + 5500
        return "El valor a pagar de la factura es {}" . format(pt)
    else:
        if estrato == 2:
            pt = 2800 + mc * 2350 + 6200
            return "El valor a pagar de la factura es {}" . format(pt)
        else:
            if estrato == 3:
                pt = 3000 + mc * 2600 + 7400
                return "El valor a pagar de la factura es {}" . format(pt)
            else:
                if estrato == 4:
                    pt = 3300 + mc * 3400 + 8600
                    return "El valor a pagar de la factura es {}" . format(pt)
                else:
                    if estrato == 5:
                        pt = 3700 + mc * 3900 + 9700
                        return "El valor a pagar de la factura es {}" . format(pt)
                    else:
                        if estrato == 6:
                            pt = 4400 + mc * 4700 + 11000
                            return "El valor a pagar de la factura es {}" . format(pt)
                        else: 
                            return "Ingrese un valor de estrato válido"
print(ejercicio_10(estrato, mc))
            