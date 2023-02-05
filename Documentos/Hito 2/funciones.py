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

    # print(f'''
    # Test R2: {r2_score(y_test, preds)}
    # Test MSE: {mean_squared_error(y_test, preds)}
    # Test Median Absolute Error: {median_absolute_error(y_test, preds)}''') 
        
    print(f'''{titulo}
    RMSE: {np.sqrt(mean_squared_error(y_test_model, preds))}
    MAE: {median_absolute_error(y_test_model, preds)}
    R2 Score: {r2_score(y_test_model, preds)}''')
        
                      
