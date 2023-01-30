from typing import List
from readCsv import readCsv
from models import true_car_listings, fuel, market_value, safety_rating, registro_unico_vin
from scraping import vincheckpro, vincheck, drivingtests, drivingtestsregistroUnico
from funciones import conexion_sqlalchemy, selectTableRegistroUnico, selectTable
import re

# conexion bd
conn = conexion_sqlalchemy()

## leer info de tabla creada en el paso anterior
# datacar = List[true_car_listings]
# datacar = selectTable(conn, 'true_car_listings', true_car_listings)

##registro unico vin
datacar = List[registro_unico_vin]
datacar = selectTableRegistroUnico(conn, registro_unico_vin)

# recorrer select * from tabla
for car in datacar:
   #vincheckpro(conn, car.Vin, car.Id)
   #drivingtests(conn, car.Vin, car.Id)
   drivingtestsregistroUnico(conn, car.Vin, car.Id)

