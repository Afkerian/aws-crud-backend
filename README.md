# aws-crud-backend

## AWS - FastAPI con CRUD de Imágenes

Este proyecto es una API construida con FastAPI que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en imágenes almacenadas en una base de datos. Utiliza Docker y Docker Compose para la gestión de contenedores y la infraestructura de la base de datos.

## ¿Quieres usar este proyecto?

Sigue los siguientes pasos para construir las imágenes y ejecutar los contenedores:

ssh:
```sh
git clone git@github.com:Afkerian/aws-crud-backend.git
```

directory:
```sh
cd aws-crud-backend/
```

docker:
```sh
docker-compose up -d --build
```

## Rutas de la API
Puedes probar las rutas siguientes en la documentación interactiva proporcionada por Swagger:

- [http://localhost:8002/docs](http://localhost:8002/docs)

## Estructura del Proyecto

- src/
    - app/
        - api/
            - images.py
        - __init__.py
        - .env
        - db.py
        - main.py
    - test/
    - Dockerfile
    - requirements.txt
    - .gitignore
    - docker-compose.yml


## Contribuciones
Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama: (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
4. Sube tus cambios (git push origin feature/nueva-funcionalidad).
5. Crea un nuevo Pull Request.

### Licencia
Este proyecto está licenciado bajo la GNU General Public License Version 3 de fecha 29 de Junio de 2007.

---

Este `README.md` proporciona una guía completa para construir, ejecutar, y usar tu proyecto FastAPI con Docker, así como una descripción de las rutas disponibles y cómo contribuir al proyecto.



