import pandas as pd

# Ejercicio 3: Agrupamiento de datos (1 punto)

# Ejercicio 3.1 (0.5 puntos)
def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
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
    
    print("Primeras cinco filas del DataFrame agrupado:")
    print(df_grouped.head(5))
    
    return df_grouped

# Ejercicio 3.2 (0.25 puntos)

# Ejercicio 3.3 (0.25 puntos)