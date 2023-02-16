import sqlalchemy as db
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

def conexion_sqlalchemy():
    """
     definición: conexion con bd postgres
          
     retorno: retorna conexion a bd    
    """
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

def selectTable(conn, table):
    '''
     definición: funcion que realiza consulta a base de datos segun la clase de modelo enviada como parametro
     
     conn: objeto conexion a la base de datos.
     classTable: nombre tabla
          
     retorno: lista con resultado de select.
    '''
    session = Session(conn)

    result = db.select(table)

    return list(session.scalars(result))