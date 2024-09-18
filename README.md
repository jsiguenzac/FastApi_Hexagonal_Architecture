FastAPI - Arquitectura Hexagonal | Joel Sigüenza
================================================

Instalación
-----------

Crear un entorno virtual, activarlo e instalar las dependencias desde el archivo requirements.txt

Usar `Command Prompt` (recomendable)

```sh
python -m venv fastapi-env
```

```sh
fastapi-env\Scripts\activate
```

```sh
pip install -r requirements.txt
```

## Es necesario tener el entorno virtual activado para:

Iniciar Servidor
----------------

```sh
uvicorn src.main:app --reload
```

Ejecutar Test
-------------

```sh
pytest -s
```