from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir conexiones
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar el modelo
try:
    model = joblib.load('modelo/modelo_antispam.pkl')
except Exception as e:
    model = None
    print(f"Error: {e}")

class CallData(BaseModel):
    duracion: int
    frecuencia: int
    prefijo: int

@app.post("/predict")
async def predict(data: CallData):
    if model is None:
        raise HTTPException(status_code=500, detail="Modelo no cargado")
    
    # Usamos model_dump() en lugar de dict()
    # Y seleccionamos solo las columnas que el modelo conoce
    df = pd.DataFrame([data.model_dump()])
    
    # IMPORTANTE: Asegúrate de que el orden sea exactamente el mismo que usaste al entrenar
    # Según tu CSV, el orden es: duracion, frecuencia, prefijo
    input_df = df[['duracion', 'frecuencia', 'prefijo']]
    
    prediction = model.predict(input_df)
    
    # 1 es spam, 0 es ham
    resultado = "SPAM" if int(prediction[0]) == 1 else "HAM"
    return {"prediction": resultado}

@app.get("/health")
async def health():
    return {"status": "ok"}