import pandas as pd

# Ejercicio 5: Análisis de los estados (1.25 puntos)

# Ejercicio 5.1 (0.25 puntos)
def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    La función agrupa los valores totales por la columna "state".
    
    Args:
        df (pd.DataFrame): DataFrame con los datos agrupados por estado y por año.
    
    Returns:
        pd.DataFrame: DataFrame con los valores agrupados solo por estado.
    """
    
    # Se quita la columna year, porque no interesa que haga la suma de esta columna
    keep_columns= ["state", "permit", "handgun", "longgun"]
    df = df[keep_columns]

    # Se agrupan los datos únicamente por estado y sumar los valores
    df_groupedby_state = df.groupby("state").sum().reset_index()

    # Mostrar las primeras cinco filas del DataFrame agrupado
    print("Primeras cinco filas del DataFrame tras la agrupación por estado:")
    print(df_groupedby_state.head(5))
    
    return df_groupedby_state


# Ejercicio 5.2 (0.25 puntos)
def clean_states(df: pd.DataFrame) -> pd.DataFrame:
    """
    La función elimina los estados Guam, Mariana Islands, Puerto Rico y Virgin Islands.

    Args:
        df (pd.DataFrame): DataFrame groupedby "state".
    
    Returns:
        pd.DataFrame: DataFrame sin los cuatro estados.
    """
    # Mostrar el número de estados antes de la eliminación
    num_states = df["state"].nunique()
    print("Número de estados diferentes ANTES de la eliminación: {}".format(num_states))

    # States a eliminar
    states_to_remove = ["Guam", "Mariana Islands", "Puerto Rico", "Virgin Islands"]
    
    # Comprobar si existen esos estados y eliminarlos
    for state in states_to_remove:
        if state in df["state"].values:
            df = df[df["state"] != state]
        else:
            raise ValueError("El estado {} no existe en el Dataframe".format(state))
            
    
    # Mostrar el número de estados diferentes tras la eliminación
    num_states = df["state"].nunique()
    print("Número de estados diferentes DESPUÉS de la eliminación: {}".format(num_states))
    
    return df

# Ejercicio 5.3 (0.25 puntos)
def merge_datasets(df_firearm: pd.DataFrame, df_population: pd.DataFrame) -> pd.DataFrame:
    """
    La función fusiona el DataFrame de datos agrupados por state con el DataFrame de population.
    
    Args:
        df_firearm (pd.DataFrame): DataFrame con los datos agrupados por estado.
        df_population (pd.DataFrame): DataFrame de population.
    
    Returns:
        pd.DataFrame: DataFrame resultante de la fusión.
    """
    
    # Fusionar los dos datasets usando la columna "state" como clave
    # Docu: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html
    # Docu: https://stackoverflow.com/questions/38256104/differences-between-merge-and-concat-in-pandas
    df_merged = pd.merge(df_firearm, df_population, how="inner", on="state")
    
    # Se muestran las cinco primeras filas del dataset fusionado
    print("Primeras cinco filas del DataFrame fusionado:")
    print(df_merged.head(5))
    
    return df_merged

# Ejercicio 5.4 (0.25 puntos)
def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    La función calcula los valores relativos de permit, longgun y handgun respecto a la población total.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos fusionados.

    Returns:
        pd.DataFrame: DataFrame con las columnas nuevas permit_perc, longgun_perc y handgun_perc.
    """
    # Se comprueba que la columna "pop_2014" existe en el DataFrame
    if "pop_2014" not in df.columns:
        raise ValueError("La columna 'pop_2014' no existe en el DataFrame.")

    # Calcular los valores relativos
    df["permit_perc"] = (df["permit"] * 100) / df["pop_2014"]
    df["longgun_perc"] = (df["longgun"] * 100) / df["pop_2014"]
    df["handgun_perc"] = (df["handgun"] * 100) / df["pop_2014"]
    
    # Se muestran las primeras cinco filas del DataFrame resultante
    print("Primeras cinco filas del DataFrame con los valores relativos:")
    print(df.head(5))
    
    return df

# Ejercicio 5.5 (0.25 puntos)
def media_55(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Se calcula la media de permit_perc
    print("\n|||| 5.5.1 ||||")
    mean_permit_perc = df['permit_perc'].mean()
    old_mean = round(mean_permit_perc, 2)
    print("Media de permit_perc (2 decimales): {}".format(old_mean))

    print("\n|||| 5.5.2 ||||")
    # 2. Mostrar información de Kentucky
    kentucky_info = df[df['code'] == 'KY']
    print("Información de Kentucky:")
    print(kentucky_info)

    print("\n|||| 5.5.3 ||||")
    # 3. Se reemplaza el valor permit_perc de Kentucky con el valor de la media
    df.loc[df['code'] == 'KY', 'permit_perc'] = mean_permit_perc
    ky_info_updated = df[df['code'] == 'KY']
    print("Información de Kentucky actualizada:")
    print(ky_info_updated)

    uh_info_updated = df[df['state'] == 'Utah']
    print("Información de Utah actualizada:")
    print(uh_info_updated)


    print("\n|||| 5.5.4 ||||")
    # Se vuelve a calcular la media con dos decimales
    mean_permit_perc_updated = df['permit_perc'].mean()
    new_mean = round(mean_permit_perc_updated, 2)
    print("Media de permit_perc actualizada (2 decimales): {}".format(round(new_mean, 2)))

    print("\n|||| 5.5.5 ||||")
    text = "El valor de la media original es {} y el de la nueva media ".format(old_mean)
    text += "media normalizada {}. \n".format(new_mean)
    text += "Hay una diferencia de más del 10%, lo cual es un cambio bastante destacable, "
    text += "contando que solo se ha modificado un valor de 51 existentes.\n"
    text += "Cuando se suprimen valores atípicos, se consigue un análisis general más preciso. "
    text += "La no eliminación de estos, tal y como se comenta en el enunciado, pueden llevar \n"
    text += "a los algoritmos de ML a conclusiones inexactas y/o erróneas."

    print(text)

    return df