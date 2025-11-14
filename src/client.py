import os
import json
import logging
from dotenv import load_dotenv
import uuid
import time
from datetime import datetime
from zoneinfo import ZoneInfo
import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
from models import session, TestData

# Cargar variables de entorno desde archivo .env
load_dotenv()

# Configuración desde variables de entorno
MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USER = os.getenv("MQTT_USER", "admin")
MQTT_PASS = os.getenv("MQTT_PASS", "admin")
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "test")

# Configurar logging (registro de eventos en la terminal)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def on_connect(client, userdata, flags, rc, properties=None):
    """Callback (función de continuación) para cuando el cliente se conecta al broker"""
    if rc == 0:
        logger.info(f"🎉 Conectado al broker MQTT en {MQTT_HOST}:{MQTT_PORT}")
        client.subscribe(MQTT_TOPIC)
        logger.info(f"Suscrito al tópico: {MQTT_TOPIC}")
    else:
        logger.error(f"Fallo al conectar al broker MQTT, código de retorno: {rc}")


def on_message(client, userdata, msg):
    """Callback para cuando se recibe un mensaje del broker"""
    try:
        topic = msg.topic
        # Intentar decodificar como UTF-8, si falla usar Latin-1
        try:
            payload = msg.payload.decode("utf-8")
        except UnicodeDecodeError:
            payload = msg.payload.decode("latin-1")

        logger.info(f"Mensaje recibido en el tópico '{topic}': {payload[:100]}...")

        # Parsear payload JSON si es aplicable
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            data = {"raw": payload}

        if "variable_1" in data and "variable_2" in data and "variable_3" in data:
            # Añadir metadatos
            data["timestamp"] = datetime.now(ZoneInfo("America/Costa_Rica"))
            data["topic"] = topic

            # Crear registro y guardar en la base de datos
            record = TestData(
                timestamp=data["timestamp"],
                topic=data["topic"],
                variable_1=data["variable_1"],
                variable_2=data["variable_2"],
                variable_3=data["variable_3"],
            )
            session.add(record)
            session.commit()  # 💾

            logger.info(f"Datos añadidos a la base de datos: {record.id}")

    except Exception as e:
        logger.error(f"Error al procesar mensaje: {e}", exc_info=True)


def on_disconnect(client, userdata, flags, rc, properties=None):
    """Callback para cuando el cliente se desconecta del broker"""
    if rc != 0:
        logger.warning(
            f"Desconexión inesperada del broker MQTT, código de retorno: {rc}"
        )
    else:
        logger.info("👋 Desconectado del broker MQTT")


def main():
    """Función principal para iniciar el suscriptor"""
    logger.info("Iniciando servicio de suscriptor MQTT...")

    # Crear cliente MQTT con callback API v2 y un ID de cliente único
    client_id = f"subscriber-{uuid.uuid4()}"
    logger.info(f"Usando ID de cliente: {client_id}")
    client = mqtt.Client(
        client_id=client_id, callback_api_version=CallbackAPIVersion.VERSION2
    )
    client.username_pw_set(MQTT_USER, MQTT_PASS)

    # Habilitar reconexión automática
    client.reconnect_delay_set(min_delay=1, max_delay=120)

    # Configurar callbacks (funciones de continuación)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    # Conectar al broker MQTT con lógica de reintentos
    max_retries = 5
    retry_delay = 5  # segundos

    for attempt in range(max_retries):
        try:
            logger.info(
                f"Intentando conectar al broker MQTT (intento {attempt + 1}/{max_retries})..."
            )
            # Aumentar keepalive a 120 segundos para prevenir desconexiones prematuras
            client.connect(MQTT_HOST, MQTT_PORT, keepalive=120)
            break
        except Exception as e:
            logger.warning(
                f"Intento de conexión MQTT {attempt + 1}/{max_retries} fallido: {e}"
            )
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                logger.error(
                    "Fallo al conectar al broker MQTT después del máximo de reintentos"
                )
                return

    # Iniciar el ciclo de procesamiento de mensajes
    try:
        logger.info("Iniciando ciclo (bucle infinito) del cliente MQTT...")
        client.loop_forever()  # ⭐️
    except KeyboardInterrupt:
        logger.info("Señal de apagado recibida")
    finally:
        client.disconnect()
        logger.info("Servicio de suscriptor finalizado 👋")


# Ejecutar la función principal si este archivo es ejecutado directamente
if __name__ == "__main__":
    main()
