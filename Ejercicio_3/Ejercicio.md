# Ejercicio: Desarrollo de API de Gestión de Usuarios y Tareas

## Objetivo
El objetivo de este ejercicio es crear una API utilizando **FastAPI** para gestionar usuarios y tareas. La API debe ser capaz de manejar autenticación mediante **tokens**, y permitir realizar acciones como crear usuarios, crear tareas, asignar tareas a usuarios, actualizar y eliminar tareas, y consultar información sobre ellos.

## Requisitos

1. **Instalación de librerías necesarias**

   Para trabajar con este ejercicio, es necesario instalar algunas librerías. Para ello, ejecuta el siguiente comando:
   ```bash
   pip install fastapi pydantic
  ```

# Generación de tokens

La autenticación se realizará mediante tokens. Debes implementar un mecanismo para generar un token único que se utilizará para autenticar las solicitudes. Este token se generará aleatoriamente, y será necesario para realizar las operaciones en la API.

# EndPoints a implementar

La aplicación debe ofrecer los siguientes endpoints:

## Crear un usuario
Permite crear un nuevo usuario en el sistema. Para ello, debe proporcionarse un nombre de usuario y una contraseña. El endpoint debe generar un token que permita autenticar al usuario en futuras interacciones.

## Obtener lista de usuarios
Este endpoint debe devolver la lista de todos los usuarios registrados. La solicitud debe ser autenticada mediante el token.

## Obtener información de un usuario específico
Este endpoint debe devolver la información de un usuario específico dado su ID.

## Eliminar un usuario
Permite eliminar un usuario del sistema a partir de su ID. El token debe ser necesario para realizar esta operación.

## Crear una tarea
Permite crear una nueva tarea. Cada tarea debe tener un título, una descripción y un estado inicial. Se debe permitir asignar tareas a usuarios mediante su ID.

## Obtener lista de todas las tareas
Este endpoint debe devolver todas las tareas registradas en el sistema.

## Asignar tarea a un usuario
Permite asignar una tarea a un usuario. Se debe indicar el ID de la tarea y el ID del usuario al que se le asignará la tarea.

## Actualizar el estado de una tarea
Este endpoint debe permitir actualizar el estado de una tarea (por ejemplo: "pendiente", "en progreso", "completada").

## Eliminar una tarea
Permite eliminar una tarea del sistema. La eliminación debe estar condicionada a que el usuario esté autorizado para eliminarla (por ejemplo, que haya sido asignada a ese usuario).

## Persistencia de Datos

Los datos de usuarios, tareas y tokens deben ser persistidos en archivos JSON. Al iniciar la aplicación, los datos deben cargarse desde estos archivos, y cualquier modificación debe ser guardada en ellos.

## Estructura de archivos:

usuarios.json: Contiene los usuarios del sistema, con su nombre de usuario, contraseña y lista de tareas asignadas.
tareas.json: Contiene las tareas del sistema, con su título, descripción, estado y usuario asignado.


# Consideraciones Adicionales

- Implementa validaciones adecuadas para los datos de entrada y manejo de errores para situaciones como: parámetros incorrectos, acceso no autorizado, tareas no encontradas, etc.

- Asegúrate de que los tokens se generen de forma aleatoria y sean únicos

- Los archivos JSON deben ser cargados y guardados correctamente para asegurar que los datos persistan entre reinicios de la aplicación.

- Los endpoints deben manejar de manera eficiente las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre usuarios y tareas.

## Ejemplo de JSON
Para la persistencia de datos, la estructura básica de los archivos JSON podría ser la siguiente:

usuarios.json

json
{
  "1": {"id": 1, "username": "usuario1", "password": "pass1", "tasks": ["1", "2"]},
  "2": {"id": 2, "username": "usuario2", "password": "pass2", "tasks": []}
}
tareas.json

json
{
  "1": {"id": 1, "title": "Tarea 1", "description": "Descripción de tarea 1", "status": "pendiente", "assigned_to": "1"},
  "2": {"id": 2, "title": "Tarea 2", "description": "Descripción de tarea 2", "status": "pendiente", "assigned_to": "1"}
}
