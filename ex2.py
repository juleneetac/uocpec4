import pandas as pd

# Ejercicio 2: Procesamiento de datos (1 punto)

# Ejercicio 2.1 (0.5 puntos)
def breakdown_date(df: pd.DataFrame) -> pd.DataFrame: 
    """
    La función divide la información que hay en la columna month creando dos nuevas columnas en el dataframe ""year" y "month".
    
    Args:
        df (pd.DataFrame): DataFrame que contiene la columna "month".
    
    Returns:
        pd.DataFrame: DataFrame con las columnas "year" y "month"
    """

    if "month" not in df.columns:
        print("Error: La columna 'month' no existe")
    
    # División de la columna "month" en "year" y "month"
    df[["year", "month"]] = df["month"].str.split("-", expand=True)
    
    # Conversión de las columnas a int
    df["year"] = df["year"].astype(int)
    df["month"] = df["month"].astype(int)
    

    print("Primeras cinco filas del DataFrame tras la separación de columnas:")
    print(df.head(5))
    
    # Devolver el DataFrame con las columnas "year" y "month" añadidas
    return df

# Ejercicio 2.2 (0.5 puntos)
def erase_month(df: pd.DataFrame) -> pd.DataFrame: 
    """
    Elimina la columna "month" y muestra las cinco primeras filas y el nombre
    de todas sus columnas.
    Returns:
    
    Args:
        df (pd.DataFrame): Dataframe que contenie la columna "month".

    Returns:
        pd.DataFrame: DataFrame sin la columna "month"
    """
    if "month" in df.columns:
        df = df.drop(columns=["month"])
        print("Columnas sin 'month':")
        print(df.columns.tolist())
        print("Primeras cinco filas del DataFrame sin 'month':")
        print(df.head())
    else:
        print("La columna 'month' no existe en el DataFrame.")
    
    return df