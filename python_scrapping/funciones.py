#from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


# def createBd():
#     # join the inputs into a complete database url.
#     url = f"mysql+pymysql://{db_user}:{db_pass}@{db_addr}/{db_name}"

#     # Create an engine object.
#     engine = create_engine(url, echo=True)

#     # Create database if it does not exist.
#     if not database_exists(engine.url):
#         create_database(engine.url)
#     else:
#         # Connect the database if exists.
#         engine.connect()

def conexion_sqlalchemy():
    '''
     definición: funcion que realiza conexion con base de datos
     
     
     retorno: conexion a base de datos postgres
    
    '''
    #local
    # user = "postgres"
    # passw = "postgre"
    # server = "localhost"
    # name_Database = "automotora"
    
    #produccion elephantsql
    user = "zdrrgzcb"
    passw = "CDGHQDhReDiEr9_ODhcMnH1Gl2hOp798"
    server = "kandula.db.elephantsql.com"
    name_Database = "zdrrgzcb"
    
    return db.create_engine(f"postgresql://{user}:{passw}@{server}/{name_Database}")


def createTableFromDataframe_sqlalchemy(dataframe, name_table):
    '''
     definición: funcion que crea tabla en base de datos segun dataframe enviado por parametro
     
     dataframe: matriz de datos que se volcara a la base de datos.
     name_table: nombre de tabla que se creara en base de datos
          
     retorno: **.
    '''
    conn = conexion_sqlalchemy()
    
    if not conn.dialect.has_table(conn.connect(), name_table):
        dataframe_temp = dataframe.copy()
        dataframe_temp.to_sql(name_table, conn)    

        
def selectTable(conn, classTable):
    '''
     definición: funcion que realiza consulta a base de datos segun la clase de modelo enviada como parametro
     
     conn: objeto conexion a la base de datos.
     classTable: nombre tabla
          
     retorno: lista con resultado de select.
    '''
    session = Session(conn)

    result = db.select(classTable).where(classTable.InformacionActualizada == False)

    return list(session.scalars(result))

def insertTable(conn, classTable):
    '''
     definición: funcion que realiza insert a base de datos segun la clase de modelo enviada como parametro
     
     conn: objeto conexion a la base de datos.
     classTable: nombre tabla
          
     retorno: **.
    
    '''
    session = Session(conn)
    session.add(classTable)
    session.commit()
    
def update_true_car_listings_table(conn, table, id):
    '''
     definición: funcion que realiza update a tabla enviada como parametro
     
     conn: objeto conexion a la base de datos.
     table: tabla de base de datos.
     id: parametro id donde se aplicara update
          
     retorno: **.
    '''
    query = f'UPDATE {table} SET "InformacionActualizada" = True WHERE {table}."Id" = {id}'    
    conn.execute(query)
    
def selectTableRegistroUnico(conn, classTable):
    '''
     definición: funcion que realiza consulta a base de datos segun la clase de modelo enviada como parametro
     
     conn: objeto conexion a la base de datos.
     classTable: nombre tabla
          
     retorno: lista con resultado de select.    
    '''
    session = Session(conn)

    result = db.select(classTable).where(classTable.InformacionActualizada == False)

    return list(session.scalars(result))    

                
