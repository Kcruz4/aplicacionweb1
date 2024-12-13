import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Análisis de Datos con Streamlit")

try:
    # Carga el archivo CSV en un DataFrame
    car_data = pd.read_csv('vehicles_us.csv')

    # Encabezado
    st.header("Gráficos interactivos con Plotly Express")

    # Botones para gráficos
    st.subheader("Usa los botones para generar gráficos:")
    
    if st.button("Mostrar histograma"):
        st.write("Histograma del kilometraje de los vehículos")
        fig_hist = px.histogram(car_data, x="odometer", title="Distribución del kilometraje")
        st.plotly_chart(fig_hist)

    if st.button("Mostrar gráfico de dispersión"):
        st.write("Gráfico de dispersión: Precio vs Kilometraje")
        fig_scatter = px.scatter(
            car_data,
            x="odometer",
            y="price",
            title="Relación entre el kilometraje y el precio",
            labels={"odometer": "Kilometraje (millas)", "price": "Precio (USD)"},
            color="type"
        )
        st.plotly_chart(fig_scatter)

    # Casillas de verificación para gráficos
    st.subheader("Usa las casillas de verificación para generar gráficos:")

    if st.checkbox("Mostrar histograma del kilometraje"):
        st.write("Histograma del kilometraje de los vehículos")
        fig_hist = px.histogram(car_data, x="odometer", title="Distribución del kilometraje")
        st.plotly_chart(fig_hist, key="unique_chart_1")



    if st.checkbox("Mostrar gráfico de dispersión: Precio vs Kilometraje"):
        st.write("Gráfico de dispersión: Precio vs Kilometraje")
        fig_scatter = px.scatter(
            car_data,
            x="odometer",
            y="price",
            title="Relación entre el kilometraje y el precio",
            labels={"odometer": "Kilometraje (millas)", "price": "Precio (USD)"},
            color="type"
        )
        st.plotly_chart(fig_scatter)

except FileNotFoundError:
    st.error("El archivo 'vehicles_us.csv' no se encontró. Asegúrate de que el archivo esté en el directorio del proyecto.")

