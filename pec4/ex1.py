import pandas as pd

# Ejercicio 1: Lectura y limpieza de datos. (0.75 puntos)

# Ejercicio 1.1. (0.25 puntos)
def read_csv(path: str, print_or_not: bool=True) -> pd.DataFrame:
    """
    Carga un archivo CSV desde un path dado y muestra las cinco primeras filas y la estructura del DataFrame.

    Args:
    url (str): El path del archivo CSV.
    print_or_not (bool):  Hacer los prints de la función. Por defecto True.

    Returns:
    pd.DataFrame: DataFrame con los datos del CSV.
    """
    df = pd.read_csv(path)
    # Utilizando este bool se tendrá la opción de printar o no.
    if print_or_not:
        # Mostrar las cinco primeras filas del DataFrame
        print("Primeras cinco filas del DataFrame:")
        print(df.head(5))

        # Mostrar la estructura del DataFrame
        print("\nEstructura del DataFrame:")
        print(df.info())
    
    # Devolver el DataFrame leído
    return df

# Ejercicio 1.2 (0.25 puntos)
def clean_csv(df: pd.DataFrame, print_or_not: bool=True) -> pd.DataFrame: 
    """
    La función limpia el DataFrame eliminando todas las columnas excepto 'month', 'state', 'permit', 'handgun', 'long_gun'.
    
    Args:
    df (pd.DataFrame): El DataFrame que será tratado.
    print_or_not (bool):  Hacer los prints de la función. Por defecto True.
    
    Returns:
    pd.DataFrame: DataFrame de salida que contiene solo las columnas necesarias.
    """
    if print_or_not:
        print("Columnas originales del DataFrame:")
        print(list(df.columns))
    
    # Mantener solo las columnas especificadas
    keep_columns= ['month', 'state', 'permit', 'handgun', 'long_gun']
    df_cleaned = df[keep_columns]

    if print_or_not:
        print("Columnas después del limpiado:")
        print(list(df_cleaned.columns))
        #print(df_cleaned.columns.tolist())
        print(df_cleaned.head(5))
    
    return df_cleaned

# Ejercicio 1.3 (0.25 puntos)
def rename_col(df, print_or_not: bool=True):
    """
    Renombra la columna "long_gun" a "longgun" en el DataFrame.
    
    Args:
    cleaned_df (pd.DataFrame): DataFrame con todas sus columnas.
    print_or_not (bool):  Hacer los prints de la función. Por defecto True.
    
    Returns:
    pd.DataFrame: DataFrame con el nombre de la columna cambiado.
    """
    # Verificar si la columna 'longgun' existe en el DataFrame
    if 'long_gun' in df.columns:
        df_column_changed = df.rename(columns={'long_gun': 'longgun'})
    else:
        raise ValueError("Error: La columna 'long_gun' no existe en el DataFrame.")
    
    if print_or_not:
        print("Nombre de la columna long_gun modificado a longgun")
        # Mostrar los nombres de todas las columnas del DataFrame
        print("Columnas actuales del DataFrame:")
        print(list(df_column_changed.columns))
    
    # Devolver el DataFrame con el nombre de la columna cambiado
    return df_column_changed
