import pandas as pd

def resumenCotizacion(fichero):
    df = pd.read_csv(fichero, sep=";", thousands=".", decimal=",", index_col=0)
    return pd.DataFrame(([df.min(), df.max(), df.mean()]), index=(["Mínimo", "Máximo", "Promedio"]))

print(resumenCotizacion("D:\Mi PC (DESKTOP-5FJTMLD)\Documents\MinTic\Ciclo1\MisionTIC-2022-R2-Ciclo1-Fundamentos_de_Programacion-main\cotizacion.csv"))