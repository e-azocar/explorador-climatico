# Proytecto Final: Explorador de Datos Climáticos

## Integrantes

- Nombre: Emmanuel Azócar
  C.I: 31.694.032
  Escuela: Matemática

- Nombre: Andrés Portilla
  C.I: 30.031.827
  Escuela: Matemática

## Descripción

El proyecto consiste en una aplicación interactiva que permite a los usuarios explorar datos climáticos de un archivo CSV. Los usuarios pueden leer el archivo, visualizar los datos en diferentes formatos (histogramas y gráficos de dispersión) y acceder a una interfaz gráfica de usuario (GUI) para una experiencia más amigable.

## Requisitos

- Python 3.8 o superior
- Pyenv (Optional, para gestionar versiones de Python)
- Archivo CSV con datos climáticos (ejemplo: `archivoTemperaturas.csv`)

## Instalación y uso

1. Crear un entorno con la versión adecuada de Python usando pyenv:
    ```bash
    pyenv install 3.13.0
    pyenv local 3.13.0
    ```

2. Instalar las bibliotecas necesarias:
    ```bash
    pip install -r requirements.txt
    ```

3. Activar `streamlit`:
    ```bash
    streamlit activate
    ```

4. Ejecutar el script principal:
   ```bash
   python main.py
   ```

## Funcionalidades

- **Leer Datos Climáticos**: Cargar datos desde un archivo CSV y almacenarlos en un DataFrame de _pandas_.
- **Calcular Promedio de Temperatura**: Calcular el promedio de la columna `AvgTemperature`.
- **Temperatura Máxima y Mínima**: Encontrar las temperaturas promedio máxima y mínima en el DataFrame.
- **Filtrar Registros**: Filtrar registros basados en un valor de temperatura promedio.
- **Visualización de Datos**: Generar histogramas y gráficos de dispersión para visualizar los datos climáticos.
- **Interfaz Gráfica de Usuario (GUI)**: Proporcionar una interfaz amigable para interactuar con los datos climáticos.

## Estructura del Proyecto

```
proyecto-intro/
├── main.py                   (Script principal que ejecuta la aplicación)
├── gui.py                    (Interfaz gráfica de usuario)
├── requirements.txt          (Lista de dependencias del proyecto)
├── archivoTemperaturas.csv   (Archivo CSV con datos climáticos)
├── README.md                 (Documentación del proyecto)
└── README.pdf                (Documentación en PDF del proyecto)
```
