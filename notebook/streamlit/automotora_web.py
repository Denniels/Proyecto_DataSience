# importar librerias
import streamlit as st
import pickle
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, AdaBoostRegressor, RandomForestRegressor, BaggingRegressor
from typing import List
from models_streamlit import make, model, state, city, fuel_type
from bd import selectTable, conexion_sqlalchemy


# -----------------------------------------------------------------------------------------------
# from pathlib import Path
# HERE = Path(__file__).parent

# Extrar los archivos pickle setting path
# model_generalista = sys.path.append('../modelos/GradientBoostingRegressor_generalista.sav')

# ------------------------------------------------------------------------------------------------

# model_generalista = 'notebook/streamlit/GradientBoostingRegressorGeneralista.sav'
# with open(model_generalista,"rb+") as gbg:
#     read_model = gbg
#     print(read_model)

def main():
    mdl_generalista = pickle.load(
        open('notebook/streamlit/modelos/RandomForestRegressor_generalista.sav', 'rb+'))
    mdl_premium1 = pickle.load(
        open('notebook/streamlit/modelos/RandomForestRegressor_premium_1.sav', 'rb+'))
    mdl_premium2 = pickle.load(
        open('notebook/streamlit/modelos/RandomForestRegressor_premium_2.sav', 'rb+'))
    mdl_premium3 = pickle.load(
        open('notebook/streamlit/modelos/BaggingRegressor_premium_3.sav', 'rb+'))
    mdl_premium4 = pickle.load(
        open('notebook/streamlit/modelos/RandomForestRegressor_premium_4.sav', 'rb+'))
    mdl_premium5 = pickle.load(
        open('notebook/streamlit/modelos/BaggingRegressor_premium_5.sav', 'rb+'))
    mdl_premium6 = pickle.load(
        open('notebook/streamlit/modelos/BaggingRegressor_premium_6.sav', 'rb+'))
    mdl_premium7 = pickle.load(open(
        'notebook/streamlit/modelos/GradientBoostingRegressor_premium_7.sav', 'rb+'))
    mdl_premium8 = pickle.load(
        open('notebook/streamlit/modelos/DecisionTreeRegressor_premium_8.sav', 'rb+'))

    # titulo
    st.title('Modelamiento Automotora Anaconda')
    st.subheader('Ingreso de Datos')

    # titulo de sidebar
    st.sidebar.header('Seleccione')

    # obtener listado de marcas desde bd
    def cargarDataMarca():
        list_marca = []

        conn = conexion_sqlalchemy()

        list_marca = selectTable(conn, make)

        conn.dispose()

        return list_marca

     # obtener listado de modelos desde bd
    def cargarDataModelos():
        list_modelo = []

        conn = conexion_sqlalchemy()

        list_modelo = selectTable(conn, model)

        conn.dispose()

        return list_modelo

    # obtener listado de estados
    def cargarDataEstados():
        list_estado = []

        conn = conexion_sqlalchemy()

        list_estado = selectTable(conn, state)

        conn.dispose()

        return list_estado

     # obtener listado de ciudades
    def cargarDataCiudad():
        list_ciudades = []

        conn = conexion_sqlalchemy()

        list_ciudades = selectTable(conn, city)

        conn.dispose()

        return list_ciudades

    def cargarDataCombustible():
        list_combustible = []

        conn = conexion_sqlalchemy()

        list_combustible = selectTable(conn, fuel_type)

        conn.dispose()

        return list_combustible

    def format_func(datalist, valueSelected):
        # for i, value in list(datalist):
        #     print(value)
        lst = list(datalist)
        fil = [x for x in lst if x.Make_Car == valueSelected]
        return fil[0].Id

    def format_func_Fuel(datalist, valueSelected):
        lst = list(datalist)
        fil = [x for x in lst if x.Fuel == valueSelected]
        return fil[0].Id

    # funcion para poner los parametros en el sidebar
    def user_input_parameters():
        dataMarca = cargarDataMarca()
        dataModelos = cargarDataModelos()
        dataEstados = cargarDataEstados()
        dataCiudad = cargarDataCiudad()
        dataCombustible = cargarDataCombustible()

        select_make = st.selectbox(
            'Selecciona marca vehiculo 👇', options=(l.Make_Car for l in dataMarca))

        select_fuel = st.selectbox(
            'Selecciona tipo combustible 👇', (l.Fuel for l in dataCombustible))

        select_model = st.selectbox(
            'Selecciona modelo vehiculo 👇', (l.Model_Car for l in dataModelos))

        select_state = st.selectbox(
            'Selecciona estado 👇', (l.State_Car for l in dataEstados))

        select_city = st.selectbox(
            'Selecciona ciudad 👇', (l.City_Car for l in dataCiudad))

        text_input_year = st.number_input(
            label="Año Vehiculo 👇",
            min_value=1990
        )

        text_input_mileage = st.number_input(
            label="ingrese millas 👇",
            min_value=0
        )

        text_input_doors = st.number_input(
            label="ingrese cantidad de puertas 👇",
            min_value=2
        )

        text_input_speed = st.number_input(
            label="ingrese número de velocidades 👇",
            min_value=4
        )

    #     sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)

        data_df = {'Year': text_input_year,
                   # 'Price':0
                   'Mileage': text_input_mileage,
                   'City_Id': 2,
                   'State_Id': 3,
                   'Make_Id': format_func(dataMarca, select_make),
                   'Model_Id': 5,
                   'Doors': text_input_doors,
                   'Fuel_Id': format_func_Fuel(dataCombustible, select_fuel),
                   'Engine_Displacement_CC': 4,
                   'Engine_Displacement_CI': 4,
                   'Engine_Number_Cylinders': 6,
                   'Transmission_Speeds': text_input_speed,
                }

        # Year-Price-Mileage-City_Id-State_Id-Make_Id-Model_Id-Doors-Fuel_Id
        # Engine_Displacement_CC-Engine_Displacement_CI-Engine_Number_Cylinders-Transmission_Speeds

        features = pd.DataFrame(data_df, index=[0])
        return features

    df = user_input_parameters()

    # escoger el modelo preferido
    option = ['Generalista', 'Premium 1', 'Premium 2', 'Premium 3',
              'Premium 4', 'Premium 5', 'Premium 6', 'Premium 7', 'Premium 8']
    model_selected = st.sidebar.selectbox(
        '¿ Selecciona clasificador ?', option)

    st.subheader(f'clasificador seleccionado: {model_selected}')
    # st.subheader(df)

    if st.button('Valorizar'):
        if model_selected == 'Generalista':
            result = mdl_generalista.predict(df)
            st.success(f'valor compra: {result}')
        if model_selected == 'Premium 1':
            result = mdl_premium1.predict(df)
            st.success(f'valor compra: {result}')
        if model_selected == 'Premium 2':
            result = mdl_premium2.predict(df)
            st.success(f'valor compra: {result}')
        if model_selected == 'Premium 3':
            result = mdl_premium3.predict(df)
            st.success(f'valor compra: {result}')
        if model_selected == 'Premium 4':
            result = mdl_premium4.predict(df)
            st.success(f'valor compra: {result}')
        if model_selected == 'Premium 5':
            result = mdl_premium5.predict(df)
            st.success(f'valor compra: {result}')
        if model_selected == 'Premium 6':
            result = mdl_premium6.predict(df)
            st.success(f'valor compra: {result}')
        if model_selected == 'Premium 7':
            result = mdl_premium7.predict(df)
            st.success(f'valor compra: {result}')
        if model_selected == 'Premium 8':
            result = mdl_premium8.predict(df)
            st.success(f'valor compra: {result}')


if __name__ == '__main__':
    main()