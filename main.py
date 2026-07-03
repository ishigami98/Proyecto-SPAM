from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir conexiones desde cualquier lugar (necesario para tu app móvil)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar el modelo (debe estar en la carpeta /modelo dentro de /backend)
model = joblib.load('modelo/modelo_antispam.pkl')

class CallData(BaseModel):
    duracion: int
    frecuencia: int
    prefijo: int

@app.post("/predict")
async def predict(data: CallData):
    # Crear el dataframe con el orden exacto de tus columnas
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)
    
    # 1 es spam, 0 es ham
    resultado = "SPAM" if prediction[0] == 1 else "HAM"
    return {"prediction": resultado}