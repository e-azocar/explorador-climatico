import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Explorador de Datos Climáticos", layout="centered")

st.title("Explorador de Datos Climáticos")
st.write("Proyecto de introducción a la computación.")

# 1. Subir archivo CSV
csv_file = st.file_uploader(
    "Suba el archivo CSV con los datos climáticos", type=["csv"]
)

if csv_file is not None:
    csv_data = pd.read_csv(csv_file)
    st.success("Datos leídos desde el archivo CSV exitosamente.")

    # 2. Calcular Promedio de Temperatura Promedio
    average_temp = csv_data["AvgTemperature"].mean()
    st.info(f"El promedio de temperatura promedio es: {average_temp:.2f}°F")

    # 3. Encontrar Temperatura Promedio Máxima
    max_temp = csv_data["AvgTemperature"].max()
    st.info(f"La temperatura promedio máxima es: {max_temp:.2f}°F")

    # 4. Encontrar Temperatura Promedio Mínima
    min_temp = csv_data["AvgTemperature"].min()
    st.info(f"La temperatura promedio mínima es: {min_temp:.2f}°F")

    # 5 y 6. Filtrar registros por temperatura promedio usando slider
    st.subheader("Filtrar registros por Temperatura Promedio")
    min_slider = float(csv_data["AvgTemperature"].min())
    max_slider = float(csv_data["AvgTemperature"].max())
    slider_range = st.slider(
        "Seleccione el rango de temperatura promedio (°F):",
        min_value=min_slider,
        max_value=max_slider,
        value=(min_slider, max_slider),
        step=0.1,
    )
    filtered = csv_data[
        (csv_data["AvgTemperature"] >= slider_range[0])
        & (csv_data["AvgTemperature"] <= slider_range[1])
    ]
    if filtered.empty:
        st.warning(
            f"No hay registros en el rango seleccionado ({slider_range[0]:.2f}°F - {slider_range[1]:.2f}°F)."
        )
    else:
        st.dataframe(filtered)

    # 7. Histograma de Temperaturas Promedio
    st.subheader("Histograma de Temperaturas Promedio")
    fig, ax = plt.subplots()
    ax.hist(csv_data["AvgTemperature"], bins=20, color="blue", alpha=0.7)
    ax.set_title("Distribución de Temperaturas Promedio")
    ax.set_xlabel("Temperatura Promedio (°F)")
    ax.set_ylabel("Frecuencia")
    st.pyplot(fig)

    # 8. Gráfico de dispersión Día vs Temperatura Promedio
    st.subheader("Gráfico de Dispersión Día vs. Temperatura Promedio")
    fig, ax = plt.subplots()
    ax.scatter(csv_data["Day"], csv_data["AvgTemperature"], color="blue", alpha=0.5)
    ax.set_title("Día vs. Temperatura Promedio")
    ax.set_xlabel("Día")
    ax.set_ylabel("Temperatura Promedio (°F)")
    st.pyplot(fig)

    # 9. Mostrar datos ingresados
    st.subheader("Datos Ingresados")
    st.dataframe(csv_data)
else:
    st.info("Por favor, suba un archivo CSV para comenzar.")
