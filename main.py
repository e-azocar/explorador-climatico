import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import os

is_running = True
csv_data = None


def show_menu():
    print("\n")
    print("--- Explorador de Datos Climáticos ---")
    print("1. Leer Datos Climáticos desde CSV")
    print("2. Calcular Promedio de Temperatura Promedio")
    print("3. Encontrar Temperatura Promedio Máxima")
    print("4. Encontrar Temperatura Promedio Mínima")
    print("5. Filtrar registros con Temperatura Promedio mayor a un valor")
    print("6. Filtrar registros con Temperatura Promedio menor a un valor")
    print("7. Generar Histograma de Temperaturas Promedio")
    print("8. Generar un gráfico de dispersión del Día vs. Temperatura Promedio")
    print("9. Mostrar Datos Ingresados")
    print("0. Salir")
    print("--------------------------------------")
    opcion = input("Seleccione una opción: ")
    return opcion


# 1. Leer Datos Climáticos desde CSV
def read_csv():
    file_path = input(
        "Ingrese la ruta del archivo .csv con los datos climáticos:"
    ).strip()
    if not file_path:
        print("No se ingresó una ruta de archivo.")
        return

    if not os.path.isfile(file_path):
        print("El archivo no existe. Por favor, verifique la ruta.")
        return

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return

    if df.empty:
        print("El archivo CSV está vacío o no se pudo leer correctamente.")
        return

    global csv_data
    csv_data = df
    print("Datos leídos desde el archivo CSV exitosamente.")


# 2. Calcular Promedio de Temperatura Promedio
def average_temperature():
    if csv_data is None:
        print("Por favor, lea los datos climáticos primero.")
        return
    average_temp = csv_data["AvgTemperature"].mean()
    print(f"El promedio de temperatura promedio es: {average_temp:.2f}°F")


# 3. Encontrar Temperatura Promedio Máxima
def max_average_temperature():
    if csv_data is None:
        print("Por favor, lea los datos climáticos primero.")
        return
    max_temp = csv_data["AvgTemperature"].max()
    print(f"La temperatura promedio máxima es: {max_temp:.2f}°F")


# 4. Encontrar Temperatura Promedio Mínima
def min_average_temperature():
    if csv_data is None:
        print("Por favor, lea los datos climáticos primero.")
        return
    min_temp = csv_data["AvgTemperature"].min()
    print(f"La temperatura promedio mínima es: {min_temp:.2f}°F")


# 5. Filtrar registros con Temperatura Promedio mayor a un valor
def filter_above_average_temperature():
    value = input("Ingrese el valor de temperatura promedio para filtrar (en °F): ")
    try:
        value = float(value)

        if csv_data is None:
            print("Por favor, lea los datos climáticos primero.")
            return
        filtered_data = csv_data[csv_data["AvgTemperature"] > value]
        if filtered_data.empty:
            print(f"No hay registros con temperatura promedio mayor a {value}°F.")
        else:
            print(
                f"Registros con temperatura promedio mayor a {value}°F:\n{filtered_data}"
            )
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")


# 6. Filtrar registros con Temperatura Promedio menor a un valor
def filter_below_average_temperature():
    if csv_data is None:
        print("Por favor, lea los datos climáticos primero.")
        return
    value = input("Ingrese el valor de temperatura promedio para filtrar (en °F): ")
    try:
        value = float(value)
        filtered_data = csv_data[csv_data["AvgTemperature"] < value]
        if filtered_data.empty:
            print(f"No hay registros con temperatura promedio menor a {value}°F.")
        else:
            print(
                f"Registros con temperatura promedio menor a {value}°F:\n{filtered_data}"
            )
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")
        return


# 7. Generar Histograma de Temperaturas Promedio
def generate_temperature_histogram():
    if csv_data is None:
        print("Por favor, lea los datos climáticos primero.")
        return

    plt.hist(csv_data["AvgTemperature"], bins=20, color="blue", alpha=0.7)
    plt.title("Distribución de Temperaturas Promedio")
    plt.xlabel("Temperatura Promedio (°F)")
    plt.ylabel("Frecuencia")
    plt.show()


# 8. Generar un gráfico de dispersión del Día vs. Temperatura Promedio
def generate_scatter_plot():
    if csv_data is None:
        print("Por favor, lea los datos climáticos primero.")
        return

    plt.scatter(csv_data["Day"], csv_data["AvgTemperature"], color="blue", alpha=0.5)
    plt.title("Gráfico de Dispersión del Día vs. Temperatura Promedio")
    plt.xlabel("Día")
    plt.ylabel("Temperatura Promedio (°F)")
    plt.show()


# 9. Mostrar Datos Ingresados
def show_data():
    if csv_data is None:
        print("Por favor, lea los datos climáticos primero.")
        return
    print("Datos ingresados:")
    print(csv_data)


# 0. Cerrar el programa
def close_program():
    print("Saliendo del Explorador de Datos Climáticos. ¡Hasta Luego!")
    global is_running
    is_running = False


menu = {
    "1": read_csv,
    "2": average_temperature,
    "3": max_average_temperature,
    "4": min_average_temperature,
    "5": filter_above_average_temperature,
    "6": filter_below_average_temperature,
    "7": generate_temperature_histogram,
    "8": generate_scatter_plot,
    "9": show_data,
    "0": close_program,
}


def main():
    print("Bienvenido al Explorador de Datos Climáticos")
    print("1. CLI (Interfaz de Línea de Comandos)")
    print("2. GUI (Interfaz Gráfica de Usuario)")
    choice = input("Seleccione una opción (por defecto 1): ").strip()

    if choice == "2":
        print("Iniciando la GUI...")
        try:
            streamlit_process = subprocess.Popen(["streamlit", "run", "gui.py"])
            input("Presione Enter para cerrar el programa...")
            streamlit_process.terminate()
            close_program()
        except subprocess.CalledProcessError as e:
            print(f"Error al iniciar la GUI: {e}")
        return

    while is_running:
        opcion = show_menu()
        if opcion in menu:
            menu[opcion]()
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()
else:
    print("Este script debe ejecutarse directamente, no como un módulo importado.")
