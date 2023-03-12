import streamlit as st
import pickle
import pandas as pd
from models_bd import make, model, state, city, fuel_type
from bd_data import selectTable, conexion_sqlalchemy, selectTableWhere
import bz2
import time
from babel.numbers import format_currency
# from localStoragePy import localStoragePy
# localStorage = localStoragePy('appanaconda', 'streamlit')

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

# obtener listado de marcas desde bd

# obtener listado de marcas desde bd


def cargarDataMarca():
    list_marca = []

    conn = conexion_sqlalchemy()

    list_marca = selectTable(conn, make)

    conn.dispose()

    return list_marca

# obtener listado de modelos desde bd


def cargarDataModelos(select_make):
    list_modelo = []

    conn = conexion_sqlalchemy()

    list_modelo = selectTable(conn, model)
    # selectTableWhere(conn, model, select_make)

    conn.dispose()
    # list_modelo = filter(lambda x: x.Make == select_make, list_modelo)
    return list_modelo

    # obtener listado de estados


def cargarDataEstados():
    list_estado = []

    conn = conexion_sqlalchemy()

    list_estado = selectTable(conn, state)

    conn.dispose()

    return list_estado

# obtener listado de ciudades
# def cargarDataCiudad():
#     list_ciudades = []

#     conn = conexion_sqlalchemy()

#     list_ciudades = selectTable(conn, city)

#     conn.dispose()

#     return list_ciudades

# def cargarDataCombustible():
#     list_combustible = []

#     conn = conexion_sqlalchemy()

#     list_combustible = selectTable(conn, fuel_type)

#     conn.dispose()

#     return list_combustible


def format_func(datalist, valueSelected):
    lst = list(datalist)
    fil = [x for x in lst if x.Make_Car == valueSelected]
    return fil[0].Id


def format_func_1(datalist, valueSelected):
    lst = list(datalist)
    fil = [x for x in lst if x.Name == valueSelected]
    return fil[0].Id


def format_func_2(datalist, valueSelected):
    # print('datalist', type(datalist))
    lst = list(datalist)
    fil = [x for x in lst if x.Model_Car == valueSelected]
    return fil[0].Id


def sesiones():
    if 'dataModelos' not in st.session_state:
        st.session_state['dataModelos'] = None
    if 'dataMarca' not in st.session_state:
        st.session_state['dataMarca'] = None
    if 'dataEstados' not in st.session_state:
        st.session_state['dataEstados'] = None
    if 'mdl_generalista' not in st.session_state:
        st.session_state['mdl_generalista'] = None
    if 'mdl_premium1' not in st.session_state:
        st.session_state['mdl_premium1'] = None
    if 'mdl_premium2' not in st.session_state:
        st.session_state['mdl_premium2'] = None
    if 'mdl_premium3' not in st.session_state:
        st.session_state.mdl_premium3 = None
    if 'mdl_premium4' not in st.session_state:
        st.session_state['mdl_premium4'] = None
    if 'mdl_premium5' not in st.session_state:
        st.session_state['mdl_premium5'] = None
    if 'mdl_premium6' not in st.session_state:
        st.session_state['mdl_premium6'] = None
    if 'mdl_premium7' not in st.session_state:
        st.session_state['mdl_premium7'] = None
    if 'mdl_premium8' not in st.session_state:
        st.session_state['mdl_premium8'] = None
    if 'ganancia' not in st.session_state:
        st.session_state['ganancia'] = None


def porcentajeError(model_selected):
    riesgo = ''

    if model_selected == 'rango desde 0 a 25.000':
        riesgo = '7%'
    if model_selected == 'rango desde 25.001 a 35.000':
        riesgo = '5%'
    if model_selected == 'rango desde 35.0001 a 45.000':
        riesgo = '4%'
    if model_selected == 'rango desde 45.001 a 55.000':
        riesgo = '3%'
    if model_selected == 'rango desde 55.001 a 65.000':
        riesgo = '3%'
    if model_selected == 'rango desde 65.001 a 75.000':
        riesgo = '3%'
    if model_selected == 'rango desde 75.001 a 85.000':
        riesgo = '2%'
    if model_selected == 'rango desde 85.001 a 95.000':
        riesgo = '2%'
    if model_selected == 'mayores a 95.001':
        riesgo = '7%'

    return riesgo


def main():
    sesiones()
    # if st.session_state.mdl_generalista == None:
    #     mdlgeneralista = bz2.BZ2File("notebook/streamlit/modelos_serializados/RandomForestRegressor_generalista.sav",'rb')
    #     mdl_generalista = pickle.load(mdlgeneralista)
    #     mdlgeneralista.close()
    #     st.session_state.mdl_generalista = mdl_generalista
    # else:
    #     mdl_generalista = st.session_state.mdl_generalista

    # if st.session_state.mdl_premium1 == None:
    #     mdlpremium1 = bz2.BZ2File("notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_1.sav",'rb')
    #     mdl_premium1 = pickle.load(mdlpremium1)
    #     mdlpremium1.close()
    #     st.session_state.mdl_premium1 = mdl_premium1
    # else:
    #     mdl_premium1 = st.session_state.mdl_premium1

    if st.session_state.mdl_premium2 == None:
        #  mdl_premium2 = pickle.load(
        #  open('notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_2.sav', 'rb+'))
        #  st.session_state.mdl_premium2 = mdl_premium2
        mdlpremium2 = bz2.BZ2File(
            "notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_2.sav", 'rb')
        mdl_premium2 = pickle.load(mdlpremium2)
        mdlpremium2.close()
        st.session_state.mdl_premium2 = mdl_premium2
    else:
        mdl_premium2 = st.session_state.mdl_premium2

    if st.session_state.mdl_premium3 is None:
        # mdl_premium3 = pickle.load(
        # open('notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_3.sav', 'rb+'))
        # st.session_state.mdl_premium3 = mdl_premium3
        mdlpremium3 = bz2.BZ2File(
            "notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_3.sav", 'rb')
        mdl_premium3 = pickle.load(mdlpremium3)
        mdlpremium3.close()
        st.session_state.mdl_premium3 = mdl_premium3
    else:
        mdl_premium3 = st.session_state.mdl_premium3

    if st.session_state.mdl_premium4 == None:
        mdlpremium4 = bz2.BZ2File(
            "notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_4.sav", 'rb')
        mdl_premium4 = pickle.load(mdlpremium4)
        mdlpremium4.close()
        st.session_state.mdl_premium4 = mdl_premium4
        # mdl_premium4 = pickle.load(
        # open('notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_4.sav', 'rb+'))
        # st.session_state.mdl_premium3 = mdl_premium4
    else:
        mdl_premium4 = st.session_state.mdl_premium4

    if st.session_state.mdl_premium5 == None:
        mdlpremium5 = bz2.BZ2File(
            "notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_5.sav", 'rb')
        mdl_premium5 = pickle.load(mdlpremium5)
        mdlpremium5.close()
        st.session_state.mdl_premium5 = mdl_premium5
        # mdl_premium5 = pickle.load(
        # open('notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_5.sav', 'rb+'))
        # st.session_state.mdl_premium5 = mdl_premium5
    else:
        mdl_premium5 = st.session_state.mdl_premium5

    if st.session_state.mdl_premium6 == None:
        mdlpremium6 = bz2.BZ2File(
            "notebook/streamlit/modelos_serializados/BaggingRegressor_premium_6.sav", 'rb')
        mdl_premium6 = pickle.load(mdlpremium6)
        mdlpremium6.close()
        st.session_state.mdl_premium6 = mdl_premium6
        # mdl_premium6 = pickle.load(
        # open('notebook/streamlit/modelos_serializados/BaggingRegressor_premium_6.sav', 'rb+'))
        # st.session_state.mdl_premium6 = mdl_premium6
    else:
        mdl_premium6 = st.session_state.mdl_premium6

    if st.session_state.mdl_premium7 == None:
        mdlpremium7 = bz2.BZ2File(
            "notebook/streamlit/modelos_serializados/GradientBoostingRegressor_premium_7.sav", 'rb')
        mdl_premium7 = pickle.load(mdlpremium7)
        mdlpremium7.close()
        st.session_state.mdl_premium7 = mdl_premium7

        # mdl_premium7 = pickle.load(open(
        # 'notebook/streamlit/modelos_serializados/GradientBoostingRegressor_premium_7.sav', 'rb+'))
        # st.session_state.mdl_premium7 = mdl_premium7
    else:
        mdl_premium7 = st.session_state.mdl_premium7

    if st.session_state.mdl_premium8 == None:
        mdlpremium8 = bz2.BZ2File(
            "notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_8.sav", 'rb')
        mdl_premium8 = pickle.load(mdlpremium8)
        mdlpremium8.close()
        st.session_state.mdl_premium8 = mdl_premium8

        # mdl_premium8 = pickle.load(
        # open('notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_8.sav', 'rb+'))
        # st.session_state.mdl_premium8 = mdl_premium8
    else:
        mdl_premium8 = st.session_state.mdl_premium8

    # titulo
    st.title('Anaconda Predict')
    st.subheader('Ingreso de Datos')

    # titulo de sidebar
    st.sidebar.header('Seleccione')

    # funcion para poner los parametros en el sidebar
    def user_input_parameters():

        if st.session_state.dataMarca == None:
            dataMarca = cargarDataMarca()
            st.session_state.dataMarca = dataMarca
        else:
            dataMarca = st.session_state.dataMarca

        select_make = st.selectbox(
            'Selecciona marca vehiculo 👇', options=(l.Make_Car for l in dataMarca))

        if st.session_state.dataModelos == None:
            dataModelos = cargarDataModelos(select_make)
            st.session_state.dataModelos = dataModelos
        else:
            dataModelos = st.session_state.dataModelos
            list_modelo = filter(lambda x: x.Make == select_make, dataModelos)
            dataModelos = list(list_modelo)

        time.sleep(2)

        select_model = st.selectbox(
            'Selecciona modelo vehiculo 👇', (l.Model_Car for l in dataModelos))

        if st.session_state.dataEstados == None:
            dataEstados = cargarDataEstados()
            st.session_state.dataEstados = dataEstados
        else:
            dataEstados = st.session_state.dataEstados

        select_state = st.selectbox(
            'Selecciona estado 👇', (l.Name for l in dataEstados))

        # dataCombustible = cargarDataCombustible()
        # select_fuel = st.selectbox(
        #     'Selecciona tipo combustible 👇', (l.Fuel for l in dataCombustible))

        # dataCiudad = cargarDataCiudad()
        # select_city = st.selectbox(
        #     'Selecciona ciudad 👇', (l.City_Car for l in dataCiudad))

        text_input_year = st.number_input(
            label="Año Vehiculo 👇",
            min_value=1997,
            max_value=2018
        )

        text_input_mileage = st.number_input(
            label="ingrese millas 👇",
            min_value=1,
            max_value=200000
        )

        text_input_CC = st.number_input(
            label="ingrese desplazamiento motor 👇",
            min_value=1,
            max_value=100
        )

        text_input_Cilindros = st.number_input(
            label="ingrese cilindros del motor 👇",
            min_value=1,
            max_value=10
        )

        st.session_state.ganancia = st.number_input(
            label="Porcentaje de ganancia", 
            min_value=1.00,
            step=2., 
            max_value=100.00,
            format="%.2f")

        data_df = {'Year': text_input_year,                
                   'Mileage': text_input_mileage,
                   # 'City_Id': 2,
                   'State_Id': format_func_1(dataEstados, select_state),
                   'Make_Id': format_func(dataMarca, select_make),
                   'Model_Id': format_func_2(dataModelos, select_model),
                   # 'Doors': text_input_doors,
                   # 'Fuel_Id': format_func_Fuel(dataCombustible, select_fuel),
                   'Engine_Displacement_CC': text_input_CC,                   
                   'Engine_Number_Cylinders': text_input_Cilindros,                
                   }

        features = pd.DataFrame(data_df, index=[0])

        return features

    df = user_input_parameters()

    # escoger el rango de precios
    # option = ['rango desde 0 a 25.000', 'rango desde 25.001 a 35.000',
    #            'rango desde 35.0001 a 45.000', 'rango desde 45.001 a 55.000',
    #            'rango desde 55.001 a 65.000', 'rango desde 65.001 a 75.000',
    #            'rango desde 75.001 a 85.000', 'rango desde 85.001 a 95.000',
    #            'mayores a 95.001']

    option = ['rango desde 35.0001 a 45.000', 'rango desde 45.001 a 55.000',
              'rango desde 55.001 a 65.000', 'rango desde 65.001 a 75.000',
              'rango desde 75.001 a 85.000', 'rango desde 85.001 a 95.000',
              'mayores a 95.001']
    
    model_selected = st.sidebar.selectbox(
        '¿ Selecciona segmento ?', option)

    riesgo = porcentajeError(model_selected)

    st.subheader(f'segmento seleccionado: {model_selected} USD')
    st.subheader(f'tasa de error del modelo: {riesgo}')
    # st.subheader(df)

    if st.button('Valorizar'):
        result = None

        # if model_selected == 'rango desde 0 a 25.000':
        #     result = mdl_generalista.predict(df)
        # if model_selected == 'rango desde 25.001 a 35.000':
        #     result = mdl_premium1.predict(df)
        if model_selected == 'rango desde 35.0001 a 45.000':
            result = mdl_premium2.predict(df)
        if model_selected == 'rango desde 45.001 a 55.000':
            result = mdl_premium3.predict(df)
        if model_selected == 'rango desde 55.001 a 65.000':
            result = mdl_premium4.predict(df)
        if model_selected == 'rango desde 65.001 a 75.000':
            result = mdl_premium5.predict(df)
        if model_selected == 'rango desde 75.001 a 85.000':
            result = mdl_premium6.predict(df)
        if model_selected == 'rango desde 85.001 a 95.000':
            result = mdl_premium7.predict(df)
        if model_selected == 'mayores a 95.001':
            result = mdl_premium8.predict(df)

        # st.success('predicción valor de compra: ${:.2f} usd'.format(result[0]))
        result_format = format_currency(result[0], 'USD', locale='en_US')
        sale_value = format_currency(
            result[0]*((float(st.session_state.ganancia)/100)+1), 'USD', locale='en_US')
        st.success(f'predicción valor de compra: {result_format} USD')
        st.success(f'valor de venta recomendado: {sale_value} USD')


if __name__ == '__main__':
    main()
