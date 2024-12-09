import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Cargar el modelo y el escalador
model = joblib.load("ensemble_model.pkl")
scaler = joblib.load("scaler.pkl")

# Título de la app
st.title("Clasificación de Clientes - Predicción de CustCat")

# Crear entradas para características
features = {
    'feature1': st.number_input("Característica 1", value=0.0),
    'feature2': st.number_input("Característica 2", value=0.0),
    'feature3': st.number_input("Característica 3", value=0.0),
    'feature4': st.number_input("Característica 4", value=0.0),
    # Añade más campos según tus características
}

# Botón de predicción
if st.button("Predecir"):
    # Convertir a DataFrame
    features_df = pd.DataFrame([features])
    scaled_features = scaler.transform(features_df)
    prediction = model.predict(scaled_features)
    st.success(f"El cliente pertenece al grupo: {prediction[0]}")
