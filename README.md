# Formato de Entrega de Ejercicios

## Estructura de la Entrega

Cada ejercicio debe ser entregado siguiendo la siguiente estructura dentro de la rama `main`:

```
/main
├── Ejercicio_1
  ├── ejercicio_x_nombre/
      ├── archivo_1.py
      ├── archivo_2.py
      ├── ...
      ├── requirements.txt (opcional)
```

### Reglas de Nomenclatura
- `ejercicio_x_nombre`: Carpeta con el nombre del ejercicio, donde `x` representa el número del ejercicio y `nombre` una breve descripción.
- Dentro de esta carpeta se incluirán todos los archivos necesarios para ejecutar el ejercicio.
- Si el ejercicio requiere librerías externas, se debe incluir un archivo `requirements.txt` con la lista de librerías y sus versiones utilizadas.

### Ejemplo de `requirements.txt`
Si el ejercicio requiere librerías, el archivo `requirements.txt` debe seguir este formato:

```
numpy==1.23.5
pandas==2.0.1
```
¡Aseguraos de seguir esta estructura para mantener el repositorio organizado y facilitar la revisión de los ejercicios! 🚀

Pd: Recomiendo que utilicéis la version 3.11.9 de python, o al menos la misma versión.
