import pandas as pd

# Ejercicio 3: Agrupamiento de datos (1 punto)

# Ejercicio 3.1 (0.5 puntos)
def groupby_state_and_year(df: pd.DataFrame, print_or_not: bool=True) -> pd.DataFrame:
    """
    La función calculaa los valores acumulados totales ("totals") agrupando los datos por año y por estado: (columnas year y state).
    
    Args:
        df (pd.DataFrame): DataFrame que contiene las columnas "year" y "state".
    
    Returns:
        pd.DataFrame: DataFrame resultante con los datos agrupados por "year" y "state".
    """
    if "year" not in df.columns or "state" not in df.columns:
        raise ValueError("Error: La columna 'year' y/o 'state' no existen.")


    # Agrupar por "year" y "state" y calcular los valores acumulados de la columna "totals"
    df_grouped = df.groupby(['year', 'state']).sum().reset_index()
    
    if print_or_not:
        print("Primeras cinco filas del DataFrame agrupado por 'year' y 'state':")
        print(df_grouped.head(5))
        
    return df_grouped

# Ejercicio 3.2 (0.25 puntos)
def print_biggest_handguns(df: pd.DataFrame) -> None:
    """
    La función imprime el estado y el año con el mayor número de handguns.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos agrupados por estado y año.
    """
    if 'handgun' not in df.columns:
        raise ValueError("El DataFrame no contiene la columna 'handgun'.")
    
    # Encontrar la fila con el mayor número de handguns
    # idxmax() para obtener el índice de la fila con el valor máximo en la columna handgun.
    # Docu: https://stackoverflow.com/questions/10202570/find-row-where-values-for-column-is-maximal-in-a-pandas-dataframe
    idx_max = df['handgun'].idxmax()
    # loc para obtener la fila con el índice idx_max.
    # Docu: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
    max_row = df.loc[idx_max]
    
    state = max_row['state']
    year = max_row['year']
    handguns = max_row['handgun']
    
    # Imprimir el mensaje informativo
    print("Mayor número de 'handguns' registrados: {} || Estado: {} || Año: {}.".format(int(handguns), state, year))

# Ejercicio 3.3 (0.25 puntos)
def print_biggest_longguns(df: pd.DataFrame) -> None:
    """
    La función imprime el estado y el año con el mayor número de longguns.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos agrupados por estado y año.
    """
    if 'longgun' not in df.columns:
        raise ValueError("El DataFrame no contiene la columna 'longgun'.")
    
    # Encontrar la fila con el mayor número de handguns
    # idxmax() para obtener el índice de la fila con el valor máximo en la columna handgun.
    idx_max = df['longgun'].idxmax()
    # loc para obtener la fila con el índice idx_max.
    max_row = df.loc[idx_max]
    
    state = max_row['state']
    year = max_row['year']
    longguns = max_row['longgun']
    
    # Imprimir el mensaje informativo
    print("Mayor número de 'longguns' registrados: {} || Estado: {} || Año: {}.".format(int(longguns), state, year))