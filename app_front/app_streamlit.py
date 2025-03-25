import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

st.title("Operaciones de Machine Learning")
st.write("Proyecto 2 - Nivel 2")
st.write("Orquestación, metricas y modelos")

# Colección de variables.  
st.write("### Registrar Dato")
col1, col2, col3 = st.columns(3)

Elevation = col1.number_input("Elevation", value=2792)
Aspect = col1.number_input("Aspect", value=60)
Slope = col1.number_input("Slope", value=10)
Horizontal_Distance_To_Hydrology = col1.number_input("Horizontal_Distance_To_Hydrology", value=543)

Vertical_Distance_To_Hydrology = col2.number_input("Vertical_Distance_To_Hydrology", value=8)
Horizontal_Distance_To_Roadways = col2.number_input("Horizontal_Distance_To_Roadways", value=1679)
Hillshade_9am = col2.number_input("Hillshade_9am", value=228)
Hillshade_Noon = col2.number_input("Hillshade_Noon", value=218)

Hillshade_3pm = col3.number_input("Hillshade_3pm", value=122)
Horizontal_Distance_To_Fire_Points = col3.number_input("Horizontal_Distance_To_Fire_Points", value=1024)
Wilderness_Area = col3.text_input("Wilderness_Area", value="Rawah")
Soil_Type = col3.text_input("Soil_Type", value="C4744")

# Ejecutar la instrucción indicada. 
click = st.button("Predecir")

# Iniciar session state
if "load_state" not in st.session_state:
    st.session_state.load_state = False

if click or st.session_state.load_state:
    st.session_state.load_state = True

    try:

        # Armar JSON con estructura de datos como lo necesita la API a consumir. 
        # Agrupa las variables en un diccionario
        datos = {
            "Elevation" :  Elevation,
            "Aspect" : Aspect,
            "Slope" : Slope,
            "Horizontal_Distance_To_Hydrology" : Horizontal_Distance_To_Hydrology,
            "Vertical_Distance_To_Hydrology" : Vertical_Distance_To_Hydrology,
            "Horizontal_Distance_To_Roadways" : Horizontal_Distance_To_Roadways,
            "Hillshade_9am" : Hillshade_9am,
            "Hillshade_Noon" : Hillshade_Noon,
            "Hillshade_3pm" : Hillshade_3pm,
            "Horizontal_Distance_To_Fire_Points" : Horizontal_Distance_To_Fire_Points,
            "Wilderness_Area" : Wilderness_Area,
            "Soil_Type" : Soil_Type
        }

        # Convierte el diccionario a una cadena JSON
        json_str = json.dumps(datos)
        # st.json(json_str)

        # Request al API generado para calcular predicción sobre dato. 
        url = 'http://10.43.101.108:8086/predict/'

        response = requests.post(url, data=json_str)

        # Plotear resultado ( con retorno de posible error )
        st.metric("resultado", value=response.text )
    except Exception as e: 
        st.metric("Falla:", value=e)

#streamlit run main.py
#Esta API debe estar expuesta en el puerto 8501.