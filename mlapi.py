from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow.keras.models import load_model

import tensorflow_decision_forests as tfdf
import json
import numpy as np
import pandas as pd

app = FastAPI()

class emission(BaseModel):
    bahanBakar : int
    jenisKendaraan : int
    jarak : float

emission_model = load_model("./model/model.h5",compile = False)

@app.get('/')
async def health():
    return {"health":"OK"}
    
@app.post('/testing')
async def predictions(item : emission):
    input_data = item.json()
    input_dic = json.loads(input_data)
    
    bb = input_dic['bahanBakar']
    jk = input_dic['jenisKendaraan']
    jr = input_dic['jarak']
    
    bbint = int(bb)
    jkint = int(jk)
    
    data = {'bahanBakar': [bbint], 'jenisKendaraan': [jkint]}
    
    df = pd.DataFrame(data)
    
    print(df)
    
    
    data_predict = tfdf.keras.pd_dataframe_to_tf_dataset(df)
    
    jumlahEmisi = emission_model.predict(data_predict)
    print("\n")
       
    print(jumlahEmisi)
    return {"Jumlah Emisi": jumlahEmisi}
