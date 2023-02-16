
from bd import selectTable, conexion_sqlalchemy
from models_streamlit import make, model, state, city, fuel_type
import inspect
import pickle

mdl_premium8 = pickle.load(open('notebook/streamlit/modelos/DecisionTreeRegressor_premium_8.sav','rb+'))
print(mdl_premium8)

def cargarDataMarca():
    list_marca = []

    conn = conexion_sqlalchemy()

    list_marca = selectTable(conn, make)

    conn.dispose()
   
    return list_marca
    
def format_func(datalist, valueSelected):
    # for i, value in list(datalist):
    #     print(value)
    lst = list(datalist)
    # fil = [x for x in lst if x.Make_Car == 'Acura'] 
    # print(fil[0].Id)
    #print(inspect.getmembers(list(datalist)))
    
    #st.write(type(datalist[0]))
    # fil = list(filter(lambda Make_Car : Make_Car == 'Acura', lst))
    # #fil = [value for value in datalist if list(datalist).Make_Car == 'Acura']
    # print(fil)
    
    

dataMarca = cargarDataMarca()
filtro = format_func(dataMarca, 'Acura') 
print(filtro)  