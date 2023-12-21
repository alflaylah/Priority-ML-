from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel


class ModelName(str, Enum):
    mobil = "Mobil"
    motor = "Motor"
    bus = "Bus"
    
app = FastAPI()


@app.get("/emisi")
async def get_model(model_name: ModelName, bbm :str):
    if model_name is ModelName.mobil and bbm == "Bensin" :
        return {"Kendaraan": model_name, "Bahan Bakar": bbm, "Hasil Emisi": 2.23}
    
    if model_name is ModelName.mobil and bbm == "Solar" :
        return {"Kendaraan": model_name, "Bahan Bakar": bbm, "Hasil Emisi": 2.8}

    if model_name is ModelName.motor and bbm == "Bensin" :
        return {"Kendaraan": model_name, "Bahan Bakar": bbm, "Hasil Emisi": 4.91}
    
    if model_name is ModelName.bus and bbm == "Bensin" :
        return {"Kendaraan": model_name, "Bahan Bakar": bbm, "Hasil Emisi": 2.801}
    
    if model_name is ModelName.bus and bbm == "Solar" :
        return {"Kendaraan": model_name, "Bahan Bakar": bbm, "Hasil Emisi": 1.610}
    
    if model_name is ModelName.motor and bbm == "Solar" :
        return {"Kendaraan": "Error"}