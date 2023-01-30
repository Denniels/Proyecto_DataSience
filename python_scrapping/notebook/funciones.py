#from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import pandas as pd

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

    strConn = f"dbname={name_Database} user={user} password={passw}"
    
    return db.create_engine(f"postgresql://{user}:{passw}@{server}/{name_Database}")


def createTableFromDataframe_sqlalchemy(dataframe, name_table):
    conn = conexion_sqlalchemy()
    
    if not conn.dialect.has_table(conn.connect(), name_table):
        dataframe_temp = dataframe.copy()
        dataframe_temp.to_sql(name_table, conn)    

        
def selectTable(conn, nameTable, classTable):
    '''
    
    '''
    session = Session(conn)

    result = db.select(classTable).where(classTable.InformacionActualizada == False)

    return list(session.scalars(result))


def selectView(conn):
    query = f'SELECT * FROM public.info_automotora'    
    #result = conn.execute(query)
    return pd.read_sql(query, conn)

def insertTable(conn, classTable):
    '''
    
    '''
    session = Session(conn)
    session.add(classTable)
    session.commit()
    
def update_true_car_listings_table(conn, table, id):
    '''
    
    '''
    query = f'UPDATE {table} SET "InformacionActualizada" = True WHERE {table}."Id" = {id}'    
    conn.execute(query)
    
def selectTableRegistroUnico(conn, classTable):
    '''
    
    '''
    session = Session(conn)

    result = db.select(classTable).where(classTable.InformacionActualizada == False)

    return list(session.scalars(result))    

                
