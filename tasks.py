from celery import Celery
from celery.schedules import timedelta
from datetime import datetime
import requests
import json
import configparser
import logging

from models import session, TestData


# Crear "app" de Celery
app = Celery("tasks", broker="redis://localhost")


# Configurar las tareas de Celery
@app.task
def test_task(url, group):
    """Descarga datos de una API y los almacena
    en la tabla de ejemplo de una base de datos.

    Parameters
    ----------
    url : str
        URL de la API.
    group : str
        Número de grupo del proyecto.

    Returns
    -------
    str
        Mensaje de éxito.
    """
    params = {"grupo": int(group)}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)

        timestamp = datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S")
        sample_size = data["sample_size"]
        for sample in range(sample_size):
            record = TestData(
                group=group,
                timestamp=timestamp,
                variable_1=data["variable_1"][sample],
                variable_2=data["variable_2"][sample],
                variable_3=data["variable_3"][sample],
            )
            session.add(record)
            session.commit()
        return "¡Hola mundo!"
    else:
        logging.error(f"Error {response.status_code}: {response.text}")
        return "Algo falló en la solicitud de datos."


@app.task
def schedule_task():
    return "¡Hola gente cada 60 minutos!"


# ----------
# Configurar aquí las tareas de Celery para el procesamiento de los datos
# ----------

# Datos de configuración
config = configparser.ConfigParser()
config.read("proyecto.cfg")
url = config["api"]["url"]
group = config["api"]["group"]
period = int(config["scheduler"]["period"])

# Configurar el planificador de tareas de Celery
app.conf.beat_schedule = {
    "test-schedule": {
        "task": "tasks.test_task",
        "args": (url, group),
        "schedule": timedelta(seconds=period),
    },
    "test-schedule-task": {
        "task": "tasks.schedule_task",
        "schedule": timedelta(minutes=60),
    },
}
