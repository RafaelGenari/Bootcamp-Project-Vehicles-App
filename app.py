import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv(
    r'C:\\Users\\Rafael\\Desktop\\Rafael\\Bootcamp\\Projects\\Bootcamp-Projects-Github\\Bootcamp-Project-Vehicles-App\\vehicles.csv')  # lendo os dados

tab1, tab2 = st.tabs(['Contagem dos tipos de carros', 'Condition x Price'])
with tab1:
    # criar um histograma
    fig = px.histogram(car_data, x='type', color='type')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
with tab2:
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x='odometer', y='condition')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

build_bar_graphic = st.checkbox(
    'Criar um gráfico de barras')  # criar um gráfico de barras

if build_bar_graphic:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de barras para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de barras
    fig = px.bar(car_data, x='type', y='transmission', color='type')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
