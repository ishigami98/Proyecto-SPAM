# AntiSpam Caller - Sistema de Detección de Llamadas Spam

Proyecto desarrollado para el curso de **Aprendizaje Estadístico** en la **Universidad Privada Antenor Orrego (UPAO)**.

## 📱 Descripción del Proyecto

Sistema inteligente diseñado para clasificar llamadas telefónicas como **SPAM** o **HAM** (legítimas) en tiempo real. La solución utiliza un modelo de *Machine Learning* entrenado con características numéricas de llamadas (duración, frecuencia y prefijo) para realizar predicciones precisas.

## 🏗 Arquitectura del Sistema

El proyecto se divide en dos componentes principales:

1. **Modelo de ML:** Clasificador basado en `RandomForest` entrenado con Python (`scikit-learn`).
2. **API Backend:** Servicio REST desarrollado con `FastAPI` que expone el modelo para inferencia.

## 🚀 Tecnologías Utilizadas

* **Lenguaje:** Python 3.9+ / Kotlin
* **Framework Backend:** FastAPI
* **Machine Learning:** Scikit-learn (RandomForest)
* **Despliegue:** Render (Cloud Service)

## 📁 Estructura del Repositorio

```text
/
├── modelo/
│   └── modelo_antispam.pkl   # Modelo entrenado
├── main.py                   # API de FastAPI
├── requirements.txt          # Dependencias del proyecto
├── .gitignore                # Archivos ignorados por Git
└── README.md                 # Documentación

```

## 🛠 Instalación y Despliegue Local

1. Clona este repositorio:
```bash
git clone https://github.com/ishigami98/Proyecto-SPAM

```


2. Instala las dependencias:
```bash
pip install -r requirements.txt

```


3. Ejecuta la API:
```bash
uvicorn main:app --reload

```


## 🧪 Pruebas del Sistema

La API cuenta con un endpoint de salud para verificar su estado:
`GET /health` -> `{"status": "ok"}`

Para realizar una predicción:
`POST /predict`

```json
{
  "duracion": 120,
  "frecuencia": 5,
  "prefijo": 9
}

```

## 👥 Integrantes (UPAO 2026)

* Rios Rios, Holger
* Carhuajulca Zaña, José
* Flores Rodriguez, Diego
* García Olivares, Junior
* Diaz Polo, Leonardo
* Bobadilla Bautista, Edward

---