FastAPI - Arquitectura Hexagonal | Joel Sigüenza
================================================

Explicación
-----------

La arquitectura empleada separa las diferentes responsabilidades en la aplicación, facilitando su mantenibilidad y escalabilidad. Esta estructura se compone de tres componentes principales:

`Núcleo (Core)`:

- Dominio: Contiene los modelos de dominio y las interfaces de repositorios, lo que representa el corazón de la lógica de negocio. Aquí se definen las entidades principales, como el modelo User, y los contratos para los repositorios, como UserRepositoryInterface.

- Casos de Uso: Encapsula la lógica de negocio mediante comandos y consultas. Esto asegura que cada acción en la aplicación, como el registro de usuarios (RegisterUser) o la obtención de datos de usuarios (GetUserById), se maneje de manera coherente y separada.

`Adaptadores`:

- Controladores: Manejan la interacción con el mundo exterior y traducen las solicitudes del cliente en comandos que el núcleo puede procesar, como el UserController.

- Repositorios: Implementan las interfaces definidas en el núcleo y gestionan el acceso a los datos, como UserRepository.

- Servicios: Proporcionan lógica adicional que no encaja directamente en el núcleo, como UserService.

`Capas Externas`:

- Configuración: Maneja la configuración del sistema, como la configuración de la base de datos en database.py. Cabe mencionar que está configurada con una base de datos alojada en Xata, se puede revisar en el archivo .env. No es necesario crear la bd de manera local ni ejecutar el script.

- Rutas: Define las rutas de la API que orquestan las solicitudes a los controladores, gestionadas por routes_manager.py.

- Esquemas: Define los esquemas de datos utilizados para la validación y serialización de los datos, como user_schema.py.

- Utilidades: Incluye funciones auxiliares y herramientas de apoyo, como helpers.py

Instalación
-----------

Crear un entorno virtual (solo si no se encuentra en la raiz del proyecto), activarlo e instalar las dependencias desde el archivo requirements.txt

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