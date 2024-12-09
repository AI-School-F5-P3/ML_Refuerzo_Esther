# Proyecto de Clasificación Multiclase - Predicción de Servicios de Clientes

![Machine Learning](https://img.shields.io/badge/Machine%20Learning-%E2%9A%99-green) ![Python](https://img.shields.io/badge/Python-%23FFD43B.svg?style=flat&logo=python&logoColor=black) ![scikit-learn](https://img.shields.io/badge/scikit%20learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar un modelo de **aprendizaje automático multiclase** para predecir el grupo de servicio de un cliente en función de sus características. La variable objetivo, `custcat`, tiene cuatro clases posibles:

- **1:** Basic Service
- **2:** E-Service
- **3:** Plus Service
- **4:** Total Service

El modelo utiliza varios algoritmos de **Machine Learning** para realizar la clasificación, incluyendo:

- Random Forest 🌲
- Gradient Boosting ⚡
- Red Neuronal (MLP) 🤖
- Support Vector Machine (SVM) 📏
- Regresión Logística Multiclase📊

Además, se implementa una técnica de **Ensemble** combinando todos los modelos para obtener la mejor precisión posible.

## Características

- **Optimización de hiperparámetros:** Usando Optuna para optimizar los hiperparámetros de los modelos. 🔧
- **Validación cruzada:** Evaluación robusta del modelo mediante validación cruzada con 5 pliegues. 🔁
- **Evaluación de modelos:** Los modelos se evalúan utilizando precisión (`accuracy`) y el informe de clasificación. 📑
- **Ensemble:** Una combinación de modelos para obtener una predicción más precisa y robusta. 🤝

## Requisitos

- Python 3.x 🐍
- scikit-learn 📚
- pandas 📊
- numpy 🔢
- optuna 🔍
- streamlit 🌐

## Instalación

1. Clonar este repositorio:

```bash
git clone https://github.com/AI-School-F5-P3/ML_Refuerzo_Esther.git
cd ML_Refuerzo_Esther
```
2. Instalar dependencias:

Para instalar las dependencias necesarias, ejecute el siguiente comando:
```bash
pip install -r requirements.txt
```

3. Implementación de Streamlit
El archivo streamlit_app.pypermite crear una aplicación interactiva donde el usuario puede ingresar las características de un cliente y obtener la predicción del grupo al que pertenece.

Para ejecutar la aplicación Streamlit, utilice el siguiente comando:

```bash
streamlit run streamlit_app.py

```



