import pandas as pd
import matplotlib.pyplot as plt

# Ejercicio 4: Análisis temporal (1 punto)

# Ejercicio 4.1 (0.75 puntos)
def time_evolution(df: pd.DataFrame) -> None:
    """
    La función crea un gráfico donde se ve un análisis temporal de "permit", "handgun" y "long_gun" desde 1998 hasta 2020.
    
    Args:
        df (pd.DataFrame): DataFrame con las columnas "year", "permit", "handgun" y "longgun".
    """
    if not {"year", "permit", "handgun", "longgun"}.issubset(df.columns):
        raise ValueError("El DataFrame debe contener las columnas 'year', 'permit', 'handgun', y 'longgun'.")
    
    # Agrupar los datos por año y sumar los valores de cada año de todos los estados
    df_grouped = df.groupby("year")[["permit", "handgun", "longgun"]].sum().reset_index()
    
    # Crear el gráfico
    plt.figure()
    
    # Plot series temporales
    # Le añado el marker para que muestre cada año con un punto
    plt.plot(df_grouped["year"], df_grouped["permit"], label="permit", marker="o")
    plt.plot(df_grouped["year"], df_grouped["handgun"], label="handgun", marker="o")
    plt.plot(df_grouped["year"], df_grouped["longgun"], label="longgun", marker="o")
    
    plt.xlabel("Year")
    plt.ylabel("Number of permits/handguns/longguns")
    plt.title("Evolución temporal de armas de fuego y licencias")
    plt.legend()
    plt.grid(True)
    # Mostrar el gráfico
    plt.show()

# Ejercicio 4.2 (0.25 puntos)
def print_42() -> None:
    """
    Printa la explicación del grafico del ejercicio 4.1

    """
    text = "Se puede observar una cierta correlación entre handgun y licencias "
    text += "sin embargo la correlación entre longgun y licencias es más difícil de interpretar"
    text += " hasta el año 2015. \n"
    text += "La tendencia de los tres datos es ascendente a lo largo de los años, viendo un máximo "
    text += "de los tres entre 2016 y 2017. Estas fechas tienen correlación con las víctimas de\n"
    text += "tiroteos masivo que comentan en la noticia proporcionada en el ejercicio. \n"
    text += "De cara a 2020, época de la pandemia, se observa una clara reducción tanto de pistolas, "
    text += "rifles y licencias.\n"
    text += "A pesar de la reducción de la pandemia, el gráfico es ascendente y en los próximos años "
    text += "se puede esperar un crecimiento."
    print(text)