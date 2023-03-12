from readCsv import readCsv
from funciones import insertTable, conexion_sqlalchemy
from models import true_car_listings, true_cars_test, true_cars_train, registro_unico_vin

# conexion bd
conn = conexion_sqlalchemy()

# leer csv base y guardar en bd local

# dfCars_true = readCsv('./Bd/archivos_csv/true_car_listings.csv', ',')

# for i, value in dfCars_true.iterrows():
#     record = true_car_listings(**{
#             'Price': value[0],
#             'Year' : value[1],
#             'Mileage' : value[2],
#             'City' : value[3],
#             'State' : value[4],
#             'Vin' : value[5],
#             'Make' : value[6],
#             'Model' : value[7],
#             'InformacionActualizada': False
#         })
#     insertTable(conn, record)

#dfCars_test = readCsv('./Bd/archivos_csv/true_cars_test.csv', ';')
# for i, value in dfCars_test.iterrows():
#      record = true_cars_test(**{
#              'Price': value[0],
#              'Year' : value[1],
#              'Mileage' : value[2],
#              'City' : value[3],
#              'State' : value[4],
#              'Vin' : value[5],
#              'Make' : value[6],
#              'Model' : value[7],
#              'InformacionActualizada': False
#          })
#      insertTable(conn, record)

# dfCars_train = readCsv('./Bd/archivos_csv/true_cars_train.csv', ';')
# for i, value in dfCars_train.iterrows():
#     record = true_cars_train(**{
#             'Price': value[0],
#             'Year' : value[1],
#             'Mileage' : value[2],
#             'City' : value[3],
#             'State' : value[4],
#             'Vin' : value[5],
#             'Make' : value[6],
#             'Model' : value[7],
#             'InformacionActualizada': False
#         })
#     insertTable(conn, record)

dfRegistroUnico = readCsv('./Bd/archivos_csv/registro_unico_vin.csv', ';')
for i, value in dfRegistroUnico.iterrows():
    record = registro_unico_vin(**{
        'Clave': value[0],
        'Make': value[1],
        'Model': value[2],
        'Vin': value[3],
        'InformacionActualizada': False
    })
    insertTable(conn, record)
