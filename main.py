from typing import Optional
from fastapi import FastAPI
from DataModel import *
from joblib import load
import pandas as pd
import numpy as np

app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
#    df.columns = dataModel.columns()
    data=prepararDatos(df)
    model = load("assets/modelo.joblib")
    result = model.predict(data)
    print(result)
    return result

def prepararDatos(data):
   columnasAnalisis=['Life expectancy','Alcohol','Hepatitis B','BMI','under-five deaths',
                  'Polio','Diphtheria','HIV/AIDS','thinness  10-19 years','Income composition of resources','Schooling']
   data=data[columnasAnalisis]
   # Se identifican las filas que tengan una esperanza de vida de 0 años, para luego quitarlas
   data['Life expectancy'].replace({0:np.nan},inplace=True)
  
   # Se eliminan las filas que reporten más de 1000 muertes de menores de 5 años por cada 1000 habitantes
   data.loc[ data['under-five deaths'] > 1000, 'under-five deaths' ] = np.nan

    #Se convierten las muertes confirmadas por VIH/SIDA por cada 1000 nios nacidos 
    #vivos en una variable binaria, que indica si hubo o casos reportados
   data.loc[ data['HIV/AIDS'] <= 1, 'HIV/AIDS' ] = 0
   data.loc[ data['HIV/AIDS'] > 1, 'HIV/AIDS' ] = 1

    #Se eliminan las filas que tengan un valor nulo
   data.dropna(inplace=True) 

   X = data.drop('Life expectancy', axis = 1)
   y = data['Life expectancy']
   return X,y



