from celery import Celery
from celery.schedules import timedelta
from datetime import datetime
import requests
import json
import configparser

from models import session, TestData

# Datos de configuración
config = configparser.ConfigParser()
config.read("proyecto.cfg")
url = config["api"]["url"]
grupo = config["api"]["grupo"]
period = int(config["scheduler"]["period"])


# Crear "app" de Celery
app = Celery("tasks", broker="redis://localhost")


# Configurar las tareas de Celery
@app.task
def test_task():
    params = {"grupo": grupo}
    response = requests.get(url, params=params)
    datos = json.loads(response.text)
    for dato in datos:
        timestamp = datetime.strptime(dato["timestamp"], "%Y-%m-%d %H:%M:%S")
        if session.query(TestData).filter_by(timestamp=timestamp).first():
            continue
        else:
            record = TestData(
                timestamp=timestamp,
                pm10=dato["sensordatavalues"][0]["value"],
                pm25=dato["sensordatavalues"][1]["value"],
                latitude=dato["location"]["latitude"],
                longitude=dato["location"]["longitude"],
                altitude=dato["location"]["altitude"],
                country=dato["location"]["country"],
            )
            session.add(record)
            session.commit()
    return "¡Hola mundo!"


@app.task
def schedule_task():
    return "¡Hola mundo cada 60 minutos!"


# ----------
# Configurar aquí las tareas de Celery para el procesamiento de los datos
# ----------

# Configurar el planificador de tareas de Celery
app.conf.beat_schedule = {
    "test-schedule": {
        "task": "tasks.test_task",
        "schedule": timedelta(seconds=period),
    },
    "test-schedule-task": {
        "task": "tasks.schedule_task",
        "schedule": timedelta(minutes=60),
    },
}
