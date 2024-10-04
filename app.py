import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv(
    r'C:\\Users\\Rafael\\Desktop\\Rafael\\Bootcamp\\Projects\\Bootcamp-Projects-Github\\Bootcamp-Project-Vehicles-App\\vehicles.csv')  # lendo os dados

# filtro para os dados de vendas de carros
columns_group = [price, model_year, model, condition, cylinders, fuel,
                 odometer, transmission, type, paint_color, is_4wd, date_posted, days_listed]

hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, columns_group)

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')  # criar um botão

if scatter_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, columns_group)

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

build_bar_graphic = st.checkbox(
    'Criar um gráfico de barras')  # criar um gráfico de barras

if build_bar_graphic:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de barras para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de barras
    fig = px.bar(car_data, columns_group)

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
