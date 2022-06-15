import pandas as pd
rutaFileCsv = 'https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv'
def listaPeliculas(rutaFileCsv: str):
    if rutaFileCsv.split('.')[-1] == 'csv':
        try:
            datos = pd.read_csv(rutaFileCsv)
            datosFiltrados = datos.filter(items=["Country", "Language", "Gross Earnings"])
            tabla = pd.pivot_table(datosFiltrados, index=["Country", "Language"])
            print(tabla.head(10))
            return(tabla.head(10))
        except:
            print("Error al leer el archivo de datos.")
    else:
        print("Extensión inválida.")

print(listaPeliculas(rutaFileCsv))