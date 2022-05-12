'''
Tres mejores amigos están en el autocine. 
En Autocinema Ukumarí, han patentado un sistema de servicio de gaseosas por botones,
en el que se puede servir una cantidad predeterminada de gaseosa según el botón presionado. 
Cada uno de ellos tiene un vaso con una capacidad dada, y ya han llenado un cierto nivel del vaso.
Como son mejores amigos, 
ellos quieren oprimir el mismo siguiente botón para servirse una cantidad fija de gaseosa en sus respectivos vasos. 
No obstante, no quieren que se les riegue la gaseosa, porque consideran que sería un desperdicio.  

Dadas la capacidad máxima de cada uno de los vasos, así como su capacidad actual, y el usuario al que pertenecen,
escriba una función que determine el nombre de la persona a la que se le regaría algo de gaseosa,
si se sirve la capacidad fija dada. Si a ninguno se le riega la gaseosa, retorne None.
Si se le riega la gaseosa a más de uno, retorne el primero en orden de parámetros pasados a la función 
(es decir, primero llena el amigo 1, luego el 2, luego el 3).

**Parámetros**  
|Nombre|Tipo|Descripción|
|-------|-----|-----|
|amigo_1|dict|Un diccionario con las siguientes llaves: "nombre", el nombre del amigo, (str) "capacidad_vaso", la capacidad máxima de su vaso, (float) "capacidad_actual", la capacidad que ha sido llenada de su vaso hasta el momento (float)|
|amigo_2|dict|Un diccionario con las siguientes llaves: "nombre", el nombre del amigo, (str) "capacidad_vaso", la capacidad máxima de su vaso, (float) "capacidad_actual", la capacidad que ha sido llenada de su vaso hasta el momento (float)|
|amigo_3|dict|Un diccionario con las siguientes llaves: "nombre", el nombre del amigo, (str) "capacidad_vaso", la capacidad máxima de su vaso, (float) "capacidad_actual", la capacidad que ha sido llenada de su vaso hasta el momento (float)|
|capacidad_boton|float|La cantidad de gaseosa que se servirá si los amigos deciden oprimir el botón correspondiente.|

|Tipo del retorno|Descripción del retorno|
|-------|-----|
|str|El nombre del amigo a quien se le riega primero la gaseosa, suponiendo un orden ascendente en cuanto a que amigo llena primero su vaso. (Es decir, primero llena el amigo 1, luego el 2, luego el 3) Si a ningun amigo se le riega la gaseosa, retorne None. Si a más de un amigo se le riega la gaseosa, retorna el primero.|
'''

amigo_1 = {
    "nombre": input("Ingrese nombre del primer amigo: "),
    "capacidad_vaso": float(300),
    "capacidad_actual": float(input("Ingrese capacidad actual de su vaso (mL): "))
}

amigo_2 = {
    "nombre": input("Ingrese nombre del segundo amigo: "),
    "capacidad_vaso": float(300), 
    "capacidad_actual": float(input("Ingrese capacidad actual de su vaso (mL): "))
}

amigo_3 = {
    "nombre": input("Ingrese nombre del tercer amigo: "),
    "capacidad_vaso": float(300), 
    "capacidad_actual": float(input("Ingrese capacidad actual de su vaso (mL): "))
}
 
capacidad_boton = 75.0

def desperdicio_de_gaseosa(amigo_1: dict, amigo_2: dict, amigo_3: dict, capacidad_boton: float):
    capacidad_final_1 = capacidad_boton + amigo_1["capacidad_actual"]
    capacidad_final_2 = capacidad_boton + amigo_2["capacidad_actual"]
    capacidad_final_3 = capacidad_boton + amigo_3["capacidad_actual"]
    if capacidad_final_1 > amigo_1["capacidad_vaso"] and capacidad_final_2 > amigo_2["capacidad_vaso"] and capacidad_final_3 > amigo_3["capacidad_vaso"]:
        return  f"A {amigo_1['nombre']}, {amigo_2['nombre']} y {amigo_3['nombre']} se les regó la gaseosa."
    elif capacidad_final_1 > amigo_1["capacidad_vaso"] and capacidad_final_2 > amigo_2["capacidad_vaso"] and capacidad_final_3 < amigo_3["capacidad_vaso"]:
        return f"A {amigo_1['nombre']} y {amigo_2['nombre']} se les regó la gaseosa, pero a {amigo_3['nombre']} no."             
    elif capacidad_final_1 > amigo_1["capacidad_vaso"] and capacidad_final_2 < amigo_2["capacidad_vaso"] and capacidad_final_3 > amigo_3["capacidad_vaso"]:
        return f"A {amigo_1['nombre']} y {amigo_3['nombre']} se les regó la gaseosa, pero a {amigo_2['nombre']} no."
    elif capacidad_final_1 > amigo_1["capacidad_vaso"] and capacidad_final_2 < amigo_2["capacidad_vaso"] and capacidad_final_3 < amigo_3["capacidad_vaso"]:
        return f"A {amigo_1['nombre']} se le regó la gaseosa, pero a {amigo_2['nombre']} y {amigo_3['nombre']} no."
    elif capacidad_final_1 < amigo_1["capacidad_vaso"] and capacidad_final_2 > amigo_2["capacidad_vaso"] and capacidad_final_3 > amigo_3["capacidad_vaso"]:
        return f"A {amigo_2['nombre']} y {amigo_3['nombre']} se les regó la gaseosa, pero a {amigo_1['nombre']} no."
    elif capacidad_final_1 < amigo_1["capacidad_vaso"] and capacidad_final_2 > amigo_2["capacidad_vaso"] and capacidad_final_3 < amigo_3["capacidad_vaso"]:
        return f"A {amigo_2['nombre']} se le regó la gaseosa, pero a {amigo_1['nombre']} y {amigo_3['nombre']} no."
    elif capacidad_final_1 < amigo_1["capacidad_vaso"] and capacidad_final_2 < amigo_2["capacidad_vaso"] and capacidad_final_3 > amigo_3["capacidad_vaso"]:
        return f"A {amigo_3['nombre']} se le regó la gaseosa, pero a {amigo_1['nombre']} y {amigo_2['nombre']} no."
    else:
        return f"A ninguno de los amigos {amigo_1['nombre']}, {amigo_2['nombre']} y {amigo_3['nombre']} se les regó la gaseosa."
print(desperdicio_de_gaseosa(amigo_1, amigo_2, amigo_3, capacidad_boton))

    

