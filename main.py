import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from xgboost import XGBRegressor

class Diamond(BaseModel):
    carat: float
    cut: str
    color: str
    clarity: str
    depth: float
    table: float
    x: float
    y: float
    z: float
    
app = FastAPI()

model = joblib.load("model.pkl")
all_columns = ['carat',
 'table',
 'volume',
 'color_D',
 'color_E',
 'color_F',
 'color_G',
 'color_H',
 'color_I',
 'color_J',
 'cut_Fair',
 'cut_Good',
 'cut_Ideal',
 'cut_Premium',
 'cut_Very Good',
 'clarity_I1',
 'clarity_IF',
 'clarity_SI1',
 'clarity_SI2',
 'clarity_VS1',
 'clarity_VS2',
 'clarity_VVS1',
 'clarity_VVS2']


@app.get("/")
def read_root():
    return {"message": "Welcome to the Diamond Price Prediction API!"}

@app.post("/predict/")
def predict(data: Diamond):
    data = pd.DataFrame([data.model_dump()])
    print(data)
    data['volume'] = data['x']*data['y']*data['z']
    data  = pd.get_dummies(data,columns = ['color','cut', 'clarity'])
    data = data.drop(columns=['depth','x','y','z'])
    for col in all_columns:
        if col not in data.columns:
            data[col] = False
    data = data[all_columns]
    print(data)
    result = model.predict(data)
    print(result)
    return float(result[0])

