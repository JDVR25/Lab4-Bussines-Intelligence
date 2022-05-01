from typing import List, Optional
from fastapi import FastAPI
from DataModel import *
from joblib import load
import pandas as pd
from DataModel2 import DataModel2
from PreProcess import prepararDatos

# Librerías para manejo de datos
import pandas as pd
pd.set_option('display.max_columns', 25) # Número máximo de columnas a mostrar
pd.set_option('display.max_rows', 50) # Numero máximo de filas a mostar
import numpy as np
np.random.seed(3301)

# Regresion lineal
from sklearn.linear_model import LinearRegression

# Metricas
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_squared_error, r2_score

app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    print(dataModel)
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    print(df)
    data=prepararDatos(df)
    model = load("assets/pipeline.joblib")
    result = model.predict(data)
    print(model)
    return result[0]

@app.post("/compare")
def make_predictions(dataModel: List[DataModel2]):
    #print(dataModel)
    data = pd.DataFrame(dataModel[0].dict(), columns=dataModel[0].dict().keys(), index=[0])
    data.columns = dataModel[0].columns()
    data = prepararDatos(data)
    for i in range(1, len(dataModel)):
      temp = dataModel[i]
      temp_el = pd.DataFrame(temp.dict(), columns=temp.dict().keys(), index=[i]) 
      temp_el.columns = temp.columns()
      temp_el=prepararDatos(temp_el)
      data = data.append(temp_el)
    
    model = load("assets/pipeline.joblib")
    y_pred = model.predict(data)
    print(y_pred)
    y_true = data['Life expectancy'].to_numpy()
    print(y_true)
    result = r2_score(y_true, y_pred)
    print(result)
    return result





