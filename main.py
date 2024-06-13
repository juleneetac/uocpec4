from ex1 import *
from ex2 import *
import argparse
#Docu args: https://stackoverflow.com/questions/42818876/python-3-argparse-call-function
# https://docs.python.org/3/library/argparse.html
#Docu pickle(save dataframe): https://www.statology.org/pandas-save-dataframe/

# python3 main.py --func read_csv  --> para escoger el nombre de la función que se quiere runnear
# python3 main.py  --> hará run de todas las funciones
path_firearm = "data/nics-firearm-background-checks.csv"
path_population = "data/us-state-populations.csv"
data_firearm = "temp_df_firearm.pkl"
data_population = "temp_df_population.pkl"

def main():

    print("\n=================")
    print("Ejercicio 1.1")
    print("=================")
    df_firearm = read_csv(path_firearm)

    print("\n=================")
    print("Ejercicio 1.2")
    print("=================")
    df_cleaned = clean_csv(df_firearm)

    print("\n=================")
    print("Ejercicio 1.3")
    print("=================")
    df_column_loggun = rename_col(df_firearm)

    print("\n=================")
    print("Ejercicio 2.1")
    print("=================")
    df_year_month=breakdown_date(df_firearm)

    print("\n=================")
    print("Ejercicio 2.2")
    print("=================")
    df_without_motnh = erase_month(df_firearm)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ejecuta funciones de la PEC.')
    
    # Añadir argumentos para cada función
    parser.add_argument('--f', type=str, help='Nombre de la función a ejecutar', default='all')
    
    # Parsear los argumentos
    args = parser.parse_args()
    
    # Ejecutar funciones basadas en los argumentos
    if args.f == 'all':
        main()
    elif args.f == 'ex1':
        print("\n=================")
        print("Ejercicio 1.1")
        print("=================")
        df_firearm = read_csv(path_firearm)
        df_firearm.to_pickle(data_firearm)

        print("\n=================")
        print("Ejercicio 1.2")
        print("=================")
        df_cleaned = clean_csv(df_firearm)

        print("\n=================")
        print("Ejercicio 1.3")
        print("=================")
        df_column_loggun = rename_col(df_firearm)

    elif args.f == 'ex2':
        print("\n=================")
        print("Ejercicio 2.1")
        print("=================")
        df_firearm_pkl = pd.read_pickle(data_firearm)
        df_year_month = breakdown_date(df_firearm_pkl)

        print("\n=================")
        print("Ejercicio 2.2")
        print("=================")
        df_without_motnh = erase_month(df_year_month)



    # elif args.f == 'clean_csv':
    #     df_firearm = read_csv(path_firearm, False)
    #     print("Ejercicio 1.2")
    #     df_cleaned = clean_csv(df_firearm)
    else:
        print(f"Función '{args.f}' no reconocida.")