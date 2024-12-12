import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Cargar el modelo y el escalador
model = joblib.load("C:/Users/Administrator/Desktop/Proyecto_ML Refuerzo/ML_Refuerzo_Esther/scr/main/ensemble_model.pkl")
scaler = joblib.load("C:/Users/Administrator/Desktop/Proyecto_ML Refuerzo/ML_Refuerzo_Esther/scr/main/scaler.pkl")


# Título de la app
st.title("Clasificación de Clientes - Predicción de CustCat")

# Crear entradas para características
name = st.text_input("Nombre")
address = st.number_input("Dirección", min_value=1, value=3)
age = st.number_input("Edad", min_value=0, value=90)
salary = st.number_input("Salario", min_value=0, value=10000)



# Botón de predicción
if st.button("Predecir"):
    if name and address:  # Verifica que las entradas de texto no estén vacías
        # Crear un diccionario de las características ingresadas
        features = {
            'name': name,
            'region': address,
            'age': age,
            'income': salary,
            
        }

        # Convertir a DataFrame 
        features_df = pd.DataFrame([features])

      
        # Escalar las características de la entrada
        scaled_features = scaler.transform(features_df)

        # Hacer la predicción
        prediction = model.predict(scaled_features)

        # Mostrar el resultado
        st.success(f"El cliente pertenece al grupo: {prediction[0]}")
    else:
        st.error("Por favor, ingresa un nombre y dirección válidos.")


'''
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Cargar el modelo y el escalador
model = joblib.load("C:/Users/Administrator/Desktop/Proyecto_ML Refuerzo/ML_Refuerzo_Esther/scr/main/ensemble_model.pkl")
scaler = joblib.load("C:/Users/Administrator/Desktop/Proyecto_ML Refuerzo/ML_Refuerzo_Esther/scr/main/scaler.pkl")

# Título de la app
st.title("Clasificación de Clientes - Predicción de CustCat")

# Crear entradas para características
features = {
    'feature1': st.number_input("address", value=0.0),
    'feature2': st.number_input("age", value=0.0),
    'feature3': st.number_input("employ", value=0.0),
    'feature4': st.number_input("gender", value=0.0),
    # Añade más campos según tus características
}

# Botón de predicción
if st.button("Predecir"):
    # Convertir a DataFrame
    features_df = pd.DataFrame([features])
    scaled_features = scaler.transform(features_df)
    prediction = model.predict(scaled_features)
    st.success(f"El cliente pertenece al grupo: {prediction[0]}")
'''