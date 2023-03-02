import streamlit as st
import pickle
import pandas as pd
from models_bd import make, model, state, city, fuel_type
from bd_data import selectTable, conexion_sqlalchemy, selectTableWhere
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
    print('cargar modelos por marca')
    list_modelo = []

    conn = conexion_sqlalchemy()

    list_modelo = selectTableWhere(conn, model, select_make)

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
    lst = list(datalist)
    # print(len(lst))
    # if len(lst) == 0:
    #     return
    fil = [x for x in lst if x.Model_Car == valueSelected]
    return fil[0].Id

def sesiones():
    if 'dataModelos' not in st.session_state:
        st.session_state['dataModelos'] = ''
    if 'dataMarca' not in st.session_state:
        st.session_state['dataMarca'] = None
    if 'dataEstados' not in st.session_state:
        st.session_state['dataEstados'] = None
    if 'mdl_generalista' not in st.session_state:
        st.session_state['mdl_generalista'] = None
    if 'mdl_premium1' not in st.session_state:
        st.session_state['mdl_premium1'] = None
    if 'mdl_premium1' not in st.session_state:
        st.session_state['mdl_premium1'] = None
    if 'mdl_premium2' not in st.session_state:
        st.session_state['mdl_premium2'] = None        
    if 'mdl_premium3' not in st.session_state:
        st.session_state['mdl_premium3'] = None      
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

           

def main():
    sesiones()   
        
    if st.session_state.mdl_generalista == None:
        mdl_generalista = pickle.load(
          open('notebook/streamlit/modelos_serializados/RandomForestRegressor_generalista.sav', 'rb+'))
        st.session_state.mdl_generalista = mdl_generalista
    else:
        mdl_generalista = st.session_state.mdl_generalista

    if st.session_state.mdl_premium1 == None:            
        mdl_premium1 = pickle.load(
        open('notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_1.sav', 'rb+'))
        st.session_state.mdl_premium1 = mdl_premium1
    else:
        mdl_premium1 = st.session_state.mdl_premium1
    
    if st.session_state.mdl_premium2 == None:            
        mdl_premium2 = pickle.load(
        open('notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_2.sav', 'rb+'))
        st.session_state.mdl_premium2 = mdl_premium2
    else:
        print('else')
        mdl_premium2 = st.session_state.mdl_premium2
                
    if st.session_state.mdl_premium3 == None:  
        mdl_premium3 = pickle.load(
        open('notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_3.sav', 'rb+'))
        st.session_state.mdl_premium3 = mdl_premium3
    else:
        mdl_premium3 = st.session_state.mdl_premium3
    
    if st.session_state.mdl_premium4 == None:      
        mdl_premium4 = pickle.load(
        open('notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_4.sav', 'rb+'))
        st.session_state.mdl_premium3 = mdl_premium4
    else:
        mdl_premium4 = st.session_state.mdl_premium4
    
    if st.session_state.mdl_premium5 == None:       
        mdl_premium5 = pickle.load(
        open('notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_5.sav', 'rb+'))
        st.session_state.mdl_premium5 = mdl_premium5
    else:
        mdl_premium5 = st.session_state.mdl_premium5
        
        
    if st.session_state.mdl_premium6 == None:           
        mdl_premium6 = pickle.load(
        open('notebook/streamlit/modelos_serializados/BaggingRegressor_premium_6.sav', 'rb+'))
        st.session_state.mdl_premium6 = mdl_premium6
    else:
        mdl_premium6 = st.session_state.mdl_premium6
    
    if st.session_state.mdl_premium7 == None:         
        mdl_premium7 = pickle.load(open(
        'notebook/streamlit/modelos_serializados/GradientBoostingRegressor_premium_7.sav', 'rb+'))
        st.session_state.mdl_premium7 = mdl_premium7
    else:
        mdl_premium7 = st.session_state.mdl_premium7
    
    if st.session_state.mdl_premium8 == None:          
        mdl_premium8 = pickle.load(
        open('notebook/streamlit/modelos_serializados/RandomForestRegressor_premium_8.sav', 'rb+'))
        st.session_state.mdl_premium8 = mdl_premium8
    else:
        mdl_premium8 = st.session_state.mdl_premium8
        
        
    # titulo
    st.title('Modelamiento Automotora Anaconda')
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
              
        
        dataModelos = cargarDataModelos(select_make)
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
            min_value=1990
        )

        text_input_mileage = st.number_input(
            label="ingrese millas 👇",
            min_value=1
        )

        text_input_CC = st.number_input(
            label="ingrese desplazamiento motor 👇",
            min_value=1
        )

        text_input_Cilindros = st.number_input(
            label="ingrese cilindros del motor 👇",
            min_value=1
        )

        # text_input_doors = st.number_input(
        #     label="ingrese cantidad de puertas 👇",
        #     min_value=2
        # )

        # text_input_speed = st.number_input(
        #     label="ingrese número de velocidades 👇",
        #     min_value=4
        # )

        # sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)

        # listfiltro_datos = ['Year','Price','Mileage', 'State_Id','Make_Id','Model_Id','Fuel_Id'
        #                     ,'Engine_Displacement_CC','Engine_Number_Cylinders']

        data_df = {'Year': text_input_year,
                   # 'Price':0
                   'Mileage': text_input_mileage,
                   # 'City_Id': 2,
                   'State_Id': format_func_1(dataEstados, select_state),
                   'Make_Id': format_func(dataMarca, select_make),
                   'Model_Id': format_func_2(dataModelos, select_model),
                   # 'Doors': text_input_doors,
                   # 'Fuel_Id': format_func_Fuel(dataCombustible, select_fuel),
                   'Engine_Displacement_CC': text_input_CC,
                   # 'Engine_Displacement_CI': 4,
                   'Engine_Number_Cylinders': text_input_Cilindros,
                   # 'Transmission_Speeds': text_input_speed,
                   }

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
