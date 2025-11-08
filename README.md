# Proyecto de programación de IE0405 - Modelos Probabilísticos de Señales y Sistemas

Los archivos incluidos en el repositorio original son:

- `mkdocs.yml`: configuración de la documentación en Material for MkDocs. Para más detalles, ver su [documentación](https://squidfunk.github.io/mkdocs-material/).
- `pyproject.toml`: especificación del proyecto y de las dependencias de paquetes de Python.
- `LICENSE`: licencia Creative Commons [Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/deed.es) de derechos de autor.
- `.gitignore`: archivos y directorios que Git ignora para hacer control de versiones y para subir a un repositorio remoto. Típicamente son archivos con datos privados o específicos del sistema operativo local, que no deben reproducirse en el repositorio de otros desarrolladores.
- `uv.lock`: parámetros del entorno de Python que será ejecutado con `uv` (más información en la [documentación de uv](https://docs.astral.sh/uv/)).

## Documentación e instrucciones del proyecto

Las instrucciones del proyecto están disponibles en la página:

[https://mpss-eie.github.io/proyecto](https://mpss-eie.github.io/proyecto)

## Instrucciones para ejecución local

Algunos de los paquetes y funcionalidades del proyecto solamente corren en los sistemas operativos tipo Unix, como Linux y macOS.

Por esta razón, las personas con Windows deben utilizar el WSL (*Windows Subsystem for Linux*) de Microsoft (o solución equivalente).

### Windows

Las [instrucciones de instalación](https://learn.microsoft.com/es-mx/windows/wsl/install) indican que solamente es necesario la siguiente instrucción en la terminal, la cual instala la distribución Ubuntu, por defecto:

```bash
wsl --install
```

Una vez en la terminal (o consola o interfaz de línea de comandos) en Linux en WSL, es necesario tener un usuario con privilegios `sudo`. Es posible configurarlo con:

```bash
adduser <username>
```

donde `<username>` puede ser, por ejemplo, `bayes` o `laplace` o `markov` o un nombre de su preferencia (`funkytomato`), y luego ingresar

```bash
usermod -aG sudo <username>
```

para actualizar los permisos. Para cambiar de usuario `root` a `<username>` y empezar una nueva sesión de terminal con ese usuario, utilizar

```bash
su <username>
```

También es recomendado utilizar la [Terminal Windows](https://learn.microsoft.com/es-es/windows/terminal/install), que ofrece mejores herramientas para manejar múltiples terminales, tanto en Windows como en el WSL. También [Warp](https://www.warp.dev/) es una terminal recomendada.

Nótese que WSL no es ni una máquina virtual ni una configuración de arranque dual (*dual boot*), sino que opera nativamente en Windows. Además, los archivos de Windows están disponibles desde Linux y viceversa.

> [!NOTE]
> Una vez instalado WSL, las instrucciones a partir de ahora aplican para una terminal Unix con `bash` o `zsh` (igual para Linux o macOS), indicado con el símbolo del *prompt* `$`.

### Clonar el repositorio

Para comenzar, es necesario "clonar" el repositorio con sus archivos localmente. Para esto:

- Asegurarse de que Git está instalado. Es posible verificar con `$ git --version`.
- Ubicarse en el directorio donde estará ubicado el proyecto, con `$ cd [PATH]`.
- Clonar el proyecto con `$ git clone https://github.com/mpss-eie/proyecto.git`.
- Moverse al directorio del proyecto con `$ cd proyecto/`.
- Si no fue hecho antes, configurar las credenciales de Git en el sistema local, con `$ git config --global user.name "Nombre Apellido"` y `$ git config --global user.email "your-email@example.com"`, de modo que quede vinculado con la cuenta de GitHub.

### Instalar `uv`

Seguir las [instrucciones de instalación](https://docs.astral.sh/uv/getting-started/installation/) de `uv` según el sistema operativo. Luego, seguir los primeros pasos de configuración, incluyendo la instalación de una versión de Python con `uv python install`. 

> [!IMPORTANT]
> La versión de Python instalada con `uv` no estará disponible localmente. En cambio, ahora es necesario ejecutar comandos como `uv run python` para abrir la línea de comandos interactiva o `uv run python [script.py]` para ejecutar un archivo.

### Crear un ambiente virtual de Python con `uv`

En una terminal, en el directorio raíz del repositorio, utilizar:

```bash
uv sync
```

Esto creará un ambiente virtual (directorio `.venv/`) e instalará las dependencias indicadas en `pyproject.toml`.

#### Instalación o remoción de paquetes

Para ser ejecutado correctamente, cada vez que un paquete nuevo sea utilizado debe ser agregado con `uv` al ambiente virtual usando:

```sh
uv add nombre-del-paquete
```

y para eliminarlo:

```sh
uv remove nombre-del-paquete
```

### Para editar y visualizar la documentación

En una terminal, en el directorio raíz del repositorio, utilizar:

```bash
uv run mkdocs serve
```

Abrir en un navegador web la página del "servidor local" en el puerto 8000, en [http://127.0.0.1:8000/](http://127.0.0.1:8000/) o en [http://localhost:8000/](http://localhost:8000/).

Cada cambio en los documentos de la carpeta `docs/` o en el archivo `mkdocs.yml` genera un refrescamiento de la página.

Para salir de la visualización, utilizar `Ctrl + C`, o, de otro modo, dejar el proceso corriendo mientras edita la documentación.

### Para ejecutar el proyecto

1. Copiar los contenidos del archivo `.env.example` en otro archivo `.env` y modificar los valores necesarios.
1. En el directorio raíz, ejecutar:

```sh
uv run src/client.py
```

## Algunas recomendaciones para Markdown

La documentación está en Markdown, que tiene muchas posibilidades.

### Ejemplo de ecuaciones matemáticas

Sea $X$ (ejemplo de una variable matemática en línea) una variable aleatoria con:

$$
x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

donde $a \neq 0$ (ejemplo de ecuación en línea).

### Ejemplo de tablas

Herramienta recomendada: [TableConvert](https://tableconvert.com/).

| Producto | Precio |
|----------|--------|
| Piña     | 1500   |
| Melón    | 1250   |
| Manzana  | 2100   |
| Papaya   | 1200   |
