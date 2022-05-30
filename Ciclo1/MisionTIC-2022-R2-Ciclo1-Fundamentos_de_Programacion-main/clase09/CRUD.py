todos = {
    1: {
        "descripcion": "Ir a mercar",
        "estado": "pendiente",
        "tiempo": 60
    },
    2: {
        "descripcion": "Estudiar",
        "estado": "pendiente",
        "tiempo": 180
    },
    3: {
        "descripcion": "Hacer ejercicio",
        "estado": "pendiente",
        "tiempo": 50
    },
    4: {
        "descripcion": "clase de programacion",
        "estado": "en curso",
        "tiempo": 120
    }
}
menuOpciones=True

#Funciones
def adicionarTarea(tareas,identificador,nuevaTarea):
    tareas[identificador]=nuevaTarea
    return tareas
def consultarTareas(tareas):
    for identificador, tarea in tareas.items():
        print(identificador, '--', end='')
        for atributo in tarea.values():
            print(atributo, '--', end='')
            print()

    


while menuOpciones:
    print('-----------------Aplicacion CRUD -----------------\n'
        '1. Adicionar Tarea -   C\n'
        '2. Consultar Tareas -  R\n'
        '3. Actualizar Tareas - U\n'
        '4. Eliminar Tarea   -  D\n'
        '5. Salir')
    opcion = int(input("Digite una opción: "))
    
    if opcion == 1:
        print('-'*10, "Adicionar Tarea", "-" *10 )
        identificador=str(input("Ingrese el identificador de la tarea: "))
        descripcion=str(input("Ingrese la descripción de la tarea: "))
        estado=str(input("Ingrese el estado de la tarea:"))
        tiempo=int(input("Ingrese el tiempo de realización: "))
        nuevaTarea={
            'descripcion': descripcion,
            'estado': estado,
            'tiempo': tiempo
        }
        tareas=adicionarTarea(tareas,identificador,nuevaTarea)
    elif opcion == 2:
        print('-'*10, "Consultar Tareas", "-" *10 )
    elif opcion == 3:
        print('-'*10, "Actualizar Tareas", "-" *10 )
    elif opcion == 4:
        print('-'*10, "Eliminar Tarea", "-" *10 )
    elif opcion == 5:
        print('-'*10, "Salir", "-" *10 )
    else:
        print("Ingrese opción válida.")        
                