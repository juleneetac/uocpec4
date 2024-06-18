from ex1 import *
from ex2 import *
from ex3 import *
from ex4 import *
from ex5 import *
from ex6 import *

import argparse
import unittest
import sys
import os

# Documentation use args: 
# https://stackoverflow.com/questions/42818876/python-3-argparse-call-function
# https://docs.python.org/3/library/argparse.html

# Documentation pickle(save dataframe): 
# https://www.statology.org/pandas-save-dataframe/

# Documentation run tests: 
# https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure


path_firearm = "data/nics-firearm-background-checks.csv"
path_population = "data/us-state-populations.csv"
data_firearm = "temp_df_firearm.pkl"
data_longgun = "temp_df_longgun.pkl"
data_without_month = "temp_df_firearm_without_month.pkl"
data_state_year = "temp_df_state_year.pkl"
data_population = "temp_df_population.pkl"
data_ky_normalized = "temp_df_ky_normalized.pkl"

def run_tests():
    # Añadir el directorio raíz del proyecto al PYTHONPATH
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, root_path)

    # Se cargan y se ejecutan los tests
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir="./tests", pattern='test_*.py')
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)

    # Si hay fallos, salir con código de error
    if not result.wasSuccessful():
        sys.exit(1)

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
    df_column_loggun = rename_col(df_cleaned)

    print("\n=================")
    print("Ejercicio 2.1")
    print("=================")
    df_year_month = breakdown_date(df_column_loggun)

    print("\n=================")
    print("Ejercicio 2.2")
    print("=================")
    df_without_month = erase_month(df_year_month)

    print("\n=================")
    print("Ejercicio 3.1")
    print("=================")
    df_grouped_state_year = groupby_state_and_year(df_without_month)

    print("\n=================")
    print("Ejercicio 3.2")
    print("=================")
    print_biggest_handguns(df_grouped_state_year)

    print("\n=================")
    print("Ejercicio 3.3")
    print("=================")
    print_biggest_longguns(df_grouped_state_year)

    print("\n=====================")
    print("Ejercicio 4.1 y 4.2")
    print("=====================")
    print_42()
    time_evolution(df_grouped_state_year)

    print("\n=================")
    print("Ejercicio 5.1")
    print("=================")
    df_grouped_state = groupby_state(df_grouped_state_year)

    print("\n=================")
    print("Ejercicio 5.2")
    print("=================")
    df_cleaned_states = clean_states(df_grouped_state)

    print("\n=================")
    print("Ejercicio 5.3")
    print("=================")
    df_population = read_csv(path_population)
    df_merged = merge_datasets(df_cleaned_states, df_population)

    print("\n=================")
    print("Ejercicio 5.4")
    print("=================")
    df_merged_perc = calculate_relative_values(df_merged)

    print("\n=================")
    print("Ejercicio 5.5")
    print("=================")
    df_ky_normalized = media_55(df_merged_perc)

    print("\n=================")
    print("Ejercicio 6")
    print("=================")
    # se utliza el datframe con el valor de permit_perc de Kentucky modificado
    print_map(df_ky_normalized, "permit_perc")
    print_map(df_ky_normalized, "longgun_perc")
    print_map(df_ky_normalized, "handgun_perc")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ejecuta funciones de la PEC.')
    
    # Añadir argumentos para cada función
    parser.add_argument('--f', type=str, help='Nombre de la función a ejecutar', default='all')
    
    # Parsear los argumentos
    args = parser.parse_args()
    
    # Ejecutar funciones basadas en los argumentos
    if args.f == 'all':
        main()

    elif args.f == 'test':
        print("\n/////////////////")
        print("Tests")
        print("/////////////////")
        run_tests()

    elif args.f == 'ex1':
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
        df_column_loggun = rename_col(df_cleaned)
        # Save pickle
        df_column_loggun.to_pickle(data_longgun)


    elif args.f == 'ex2':
        print("\n=================")
        print("Ejercicio 2.1")
        print("=================")
        # load pickle
        df_longgun_pkl = pd.read_pickle(data_longgun)
        df_year_month = breakdown_date(df_longgun_pkl)

        print("\n=================")
        print("Ejercicio 2.2")
        print("=================")
        df_without_month = erase_month(df_year_month)
        # save pickle
        df_without_month.to_pickle(data_without_month)

    elif args.f == 'ex3':
        print("\n=================")
        print("Ejercicio 3.1")
        print("=================")
        # load pickle
        df_without_month_pkl = pd.read_pickle(data_without_month)
        df_grouped_state_year = groupby_state_and_year(df_without_month_pkl)
        # save pickle
        df_grouped_state_year.to_pickle(data_state_year)

        print("\n=================")
        print("Ejercicio 3.2")
        print("=================")
        print_biggest_handguns(df_grouped_state_year)

        print("\n=================")
        print("Ejercicio 3.3")
        print("=================")
        print_biggest_longguns(df_grouped_state_year)
    
    elif args.f == 'ex4':
        print("\n=====================")
        print("Ejercicio 4.1 y 4.2")
        print("=====================")
        # load pickle
        df_state_year_pkl = pd.read_pickle(data_state_year)
        print_42()
        time_evolution(df_state_year_pkl)

    elif args.f == 'ex5':
        print("\n=================")
        print("Ejercicio 5.1")
        print("=================")
        # load pickle
        df_state_year_pkl = pd.read_pickle(data_state_year)
        df_grouped_state = groupby_state(df_state_year_pkl)

        print("\n=================")
        print("Ejercicio 5.2")
        print("=================")
        df_cleaned_states = clean_states(df_grouped_state)

        print("\n=================")
        print("Ejercicio 5.3")
        print("=================")
        df_population = read_csv(path_population)
        df_merged = merge_datasets(df_cleaned_states, df_population)

        print("\n=================")
        print("Ejercicio 5.4")
        print("=================")
        df_merged_perc = calculate_relative_values(df_merged)

        print("\n=================")
        print("Ejercicio 5.5")
        print("=================")
        df_ky_normalized = media_55(df_merged_perc)
        # save pickle
        df_ky_normalized.to_pickle(data_ky_normalized)

    elif args.f == 'ex6':
        print("\n=================")
        print("Ejercicio 6")
        print("=================")
        # load pickle
        df_ky_normalized_pkl = pd.read_pickle(data_ky_normalized)
        # se utliza el datframe con el valor de permit_perc de Kentucky modificado
        print_map(df_ky_normalized_pkl, "permit_perc")
        print_map(df_ky_normalized_pkl, "longgun_perc")
        print_map(df_ky_normalized_pkl, "handgun_perc")

    else:
        print(f"Función '{args.f}' no reconocida.")
