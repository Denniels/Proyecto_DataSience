#from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import pandas as pd
import scipy.stats as stats
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, median_absolute_error, r2_score, confusion_matrix
import numpy as np

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

        
def selectViewTrain(conn):
    query = f'SELECT * FROM public.info_automotora_train'    

    return pd.read_sql(query, conn)

def selectViewTest(conn):
    query = f'SELECT * FROM public.info_automotora_test'    

    return pd.read_sql(query, conn)


def selectViewComplete(conn):
    query = f'SELECT * FROM public.info_automotora_listings'    

    return pd.read_sql(query, conn)


def remove_outlier(df_in, col_name, f_rango):
    '''
    definición: Método de rango intercuartílico para eliminar valores atípicos
                El rango intercuartil (IQR) es la diferencia entre el percentil 75 (Q3) y el percentil 25 (Q1) 
                en un conjunto de datos. Mide la dispersión del 50% medio de los valores. 
                Puede definir una observación como un valor atípico si es f_rango veces 
                el rango intercuartílico mayor que el tercer cuartil (Q3) o f_rango veces 
                el rango intercuartílico menor que el primer cuartil (Q1).
                
                IQR-distancia desde la mediana.
                elimina todos los datos que estén a más de f_rango veces el rango intercuartílico de 
                distancia de la mediana de los datos.
                
    retorno: dataframe sin outliers            
    '''
    q1 = df_in[col_name].quantile(0.25)
    q3 = df_in[col_name].quantile(0.75)
    #iqr = q3-q1 #Interquartile range
    iqr = df_in[col_name].apply(stats.iqr) #Solo mantenemos filas que esten dentro de f_rango*IQR del Q1 y Q3
    fence_low  = q1-f_rango*iqr
    fence_high = q3+f_rango*iqr
    df_out = df_in[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]    
    return df_out

def boxplot_graph(X, Y, Title):
    boxplot = sns.boxplot(x=X, y=Y)
    boxplot.axes.set_title(Title, fontsize=16)
    boxplot.set_xlabel("Make", fontsize=14)
    boxplot.set_ylabel("Price", fontsize=14)
    plt.xticks(rotation=90) 
    plt.show()

def report_metrics(model, dataframeTrain, dataframeTest, vector_objetivo, titulo):
    dfTempTrain = dataframeTrain.copy()
    dfTempTest = dataframeTest.copy()
    
    X_train_model = dfTempTrain.drop(columns = [vector_objetivo])
    y_train_model = dfTempTrain[vector_objetivo]

    X_test_model = dfTempTest.drop(columns = [vector_objetivo])
    y_test_model = dfTempTest[vector_objetivo]
    
    clf_model = model.fit(X_train_model, y_train_model)
    
    preds = clf_model.predict(X_test_model)
        
    print(f'''{titulo}
    RMSE: {np.sqrt(mean_squared_error(y_test_model, preds))}
    MAE: {median_absolute_error(y_test_model, preds)}
    R2 Score: {r2_score(y_test_model, preds)}''')
    

def graph(dataframe):
    dfTemp = dataframe.copy()
    rows = 1
    cols = 1
    
    if dfTemp.shape[1] != 1:
        rows = 2
        cols = dfTemp.shape[1] // rows

    for index, (colnames, serie) in enumerate(dfTemp.iteritems()):
        plt.subplot(rows, cols, index + 1)
        if serie.dtype == 'object':
            sns.countplot(serie.dropna())
            plt.axhline(serie.value_counts().mean(), color='forestgreen',linestyle='--')
            plt.title(colnames)
        else:
            sns.distplot(serie.dropna(), color='slategrey')
            plt.axvline(serie.mean(), color='forestgreen', linestyle='--')
            plt.title(colnames)

    plt.xticks(rotation=90) 
    plt.tight_layout()
