# Proyecto de programación de IE0405 - Modelos Probabilísticos de Señales y Sistemas

Los archivos incluidos en el repositorio original son:

- `mkdocs.yml`: configuración de la documentación en Material for MkDocs. Para más detalles, ver su [documentación](https://squidfunk.github.io/mkdocs-material/).
- `requirements.txt`: especificación de las dependencias de paquetes de Python.
- `LICENSE`: licencia Creative Commons [Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/deed.es) de derechos de autor.
- `.gitignore`: archivos y directorios que Git ignora para hacer control de versiones y para subir a un repositorio remoto. Típicamente son archivos con datos privados o específicos del sistema operativo local, que no deben reproducirse en el repositorio de otros desarrolladores.

## Documentación e instrucciones del proyecto

Las intrucciones del proyecto están disponibles en la página:

[https://mpss-eie.github.io/proyecto](https://mpss-eie.github.io/proyecto)

## Instrucciones para ejecución local

Algunos de los paquetes y funcionalidades del proyecto solamente operan en los sistemas operativos tipo Unix, como Linux y macOS.

Por esta razón, las personas con Windows deben utilizar WSL (*Windows Subsystem for Linux*).

Las [instrucciones de instalación](https://learn.microsoft.com/es-mx/windows/wsl/install) indican que solamente es necesario la siguiente instrucción en la terminal, que instala Ubuntu por defecto:

```bash
wsl --install
```

Una vez en la terminal (o consola o interfaz de línea de comandos) en Linux en WSL, es necesario tener un usuario con privilegios `sudo`. Es posible configurarlo con:

```bash
adduser <username>
```

donde `<username>` puede ser, por ejemplo, `bayes` o `laplace` o `markov` o un nombre de su preferencia, y luego

```bash
usermod -aG sudo <username>
```

para actualizar los permisos. Para cambiar de usuario `root` a `<username>` y empezar una nueva sesión de terminal con ese usuario, utilizar

```bash
su <username>
```

También es recomendado utilizar la [Terminal Windows](https://learn.microsoft.com/es-es/windows/terminal/install), que ofrece mejores herramientas para manejar múltiples terminales, tanto en Windows como en el WSL. 

Nótese que WSL no es ni una máquina virtual ni una configuración de arranque dual (*dual boot*), sino que opera nativamente en Windows. Además, los archivos de Windows están disponibles desde Linux y viceversa.

Una vez instalado WSL, las instrucciones a partir de ahora aplican para una terminal Unix con `bash` o `zsh`, indicado con el símbolo *prompt* `$`.

### Clonar el repositorio

Para comenzar, es necesario "clonar" el repositorio con sus archivos localmente. Para esto:

- Asegurarse de que Git está instalado. Es posible probar con `$ git --version`.
- Ubicarse en el directorio donde estará ubicado el proyecto, con `$ cd`.
- Clonar el proyecto con `$ git clone https://github.com/mpss-eie/proyecto.git`.
- Moverse al directorio del proyecto con `$ cd proyecto/`.
- Si no fue hecho antes, configurar las credenciales de Git en el sistema local, con `$ git config --global user.name "Nombre Apellido"` y `$ git config --global user.email "your-email@example.com"`, de modo que quede vinculado con la cuenta de GitHub.

### Crear un ambiente virtual de Python

En una terminal, en el directorio raíz del repositorio, utilizar:

```bash
python3 -m venv env
```

donde `env` es el nombre del ambiente. Esto crea una carpeta con ese nombre.

Para activar el ambiente virtual, utilizar:

```bash
source env/bin/activate
```

donde `env/bin/activate` es el `PATH`. El *prompt* de la terminal cambiará para algo similar a:

```bash
base env ~/.../pipeline $
```

En este ambiente virtual no hay paquetes de Python instalados. Es posible verificar esto con `pip list`, que devolverá algo como:

```bash
Package    Version
---------- -------
pip        24.0
setuptools 65.5.0
```

### Instalar los paquetes necesarios para ejecutar el proyecto

Con el ambiente virtual activado, instalar los paquetes indicados en el archivo `requirements.txt`, con:

```bash
pip install -r requirements.txt
```

Para verificar la instalación, es posible usar nuevamente `pip list`, que ahora mostrará una buena cantidad de nuevos paquetes y sus dependencias.

### Para editar y visualizar la documentación

En una terminal, en el directorio raíz del repositorio, utilizar:

```bash
mkdocs serve
```

Abrir en un navegador web la página del "servidor local" en el puerto 8000, en [http://127.0.0.1:8000/](http://127.0.0.1:8000/) o en [http://localhost:8000/](http://localhost:8000/).

Cada cambio en los documentos de la carpeta `docs/` o en el archivo `mkdocs.yml` genera un refrescamiento de la página.

Para salir de la visualización, utilizar `Ctrl + C`, de otro modo dejar el proceso corriendo mientras edita la documentación.

### Para ejecutar el proyecto

- En el directorio raíz, crear un archivo `proyecto.cfg` con el siguiente contenido:

```
[api]
url = https://kalouk.xyz/api/datos
group = 000

[db]
db = sqlite
sqlite = sqlite:///proyecto.db
postgresql = postgresql://localhost:5432/proyecto

[scheduler]
period = 15
```

y modificar según las necesidades de su implementación. Es recomendable mantener un archivo de configuración con las variables separadas del código, para no *hard-codear*-las.

- En una nueva terminal ejecutar el siguiente comando para activar **Redis** (más detalles en la documentación): 

```bash
redis-server
```

dejar esta terminal "corriendo".

Nota: en sistemas Linux usualmente ya está corriendo como *servicio del sistema* y por tanto dará un error de que ya está ocupado el proceso. En ese caso es posible ignorar este paso.

- En una nueva terminal ejecutar el siguiente comando para activar **Celery Worker** (más detalles en la documentación):

```bash
celery --app tasks worker --loglevel=INFO
```

dejar esta terminal "corriendo". 

**Nota**: cada vez que haya cambios en `tasks.py` debe reiniciarse este proceso (Ctrl + C para detener).

- En una nueva terminal ejecutar el siguiente comando para activar **Celery Beat** (más detalles en la documentación):

```bash
celery --app tasks beat --loglevel=INFO
```

dejar esta terminal "corriendo".

En este punto, ya el código de ejemplo debería estar importando y guardando datos en la base de datos, según está detallado en `models.py` y `tasks.py`.

**Nota**: para hacer una sola prueba de la función (`@app.task`) y no activar Celery Beat, es posible utilizar en la terminal, en el mismo directorio que `tasks.py`:

```bash
$ python
>>> from tasks import test_task
>>> url = "https://kalouk.xyz/api/datos"
>>> group = "000"
>>> test_task.delay(url, group)
```

Es decir, utilizar Python para importar la función `test_task` (o la función de su proyecto) y ejecutar el método `.delay()` para ejecución sincrónica ("en el momento").
