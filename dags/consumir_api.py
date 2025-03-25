from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests
import csv

# Definir la función para obtener datos desde la API y guardarlos en un archivo CSV
def fetch_data():
    api_url = "http://10.43.101.108/datos"  # URL de la API
    csv_file = "datos/covertype.csv"  # Archivo donde se almacenarán los datos

    response = requests.get(api_url)  # Realizar la solicitud a la API
    data = response.json()["datos"]  # Extraer los datos en formato JSON

    # Abrir el archivo CSV en modo de escritura y agregar nuevas filas
    with open(csv_file, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)  # Escribir cada fila en el archivo CSV

# Definir el DAG (Directed Acyclic Graph) en Airflow
with DAG(
    "api_to_csv",  # Nombre del DAG
    description="Fetch data from the covertype API and save in file",  # Descripción del DAG
    start_date=datetime(2025, 3, 24),  # Fecha de inicio de la ejecución
    end_date=datetime(2026, 3, 24, 1),  # Fecha de finalización de la ejecución
    schedule_interval=timedelta(minutes=1),  # Intervalo de ejecución (cada 1 minuto)
):
    # Crear la tarea que ejecutará la función fetch_data
    get_data_task = PythonOperator(
        task_id="fetch_data",  # Identificador de la tarea
        python_callable=fetch_data  # Función a ejecutar
    )

    # Definir la secuencia de ejecución de la tarea
    get_data_task
