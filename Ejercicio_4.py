#importamos streamlit , pandas , matplotlib y numpy

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Visualización de Casos por Edad Etaria por Sexo de Covid-19 ")
st.markdown("## Grafico de datos en forma de Grupo Etario por Sexo")


df=pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto16/CasosGeneroEtario.csv")
st.sidebar.markdown("### Grafico 1")
Grupo_edad=st.sidebar.selectbox("Grupo Etario", df["Grupo de edad"].unique())
st.markdown("su seleccion es: " + Grupo_edad)
Sexo=st.sidebar.selectbox("Sexo", df.Sexo.unique())
st.markdown("su seleccion es: " + Sexo)
superfiltro=df[(df["Grupo de edad"]==Grupo_edad)&(df.Sexo==Sexo)]
fig,ax = plt.subplots()
to_plot=superfiltro.iloc[:,2:-1]
ax.plot(to_plot.T)
ax.set_title(Grupo_edad)
ax.set_ylabel(Sexo)
ax.set_xlabel("Fecha")
xs= np.arange(0,superfiltro.shape[1]-2,30)
plt.xticks(xs,rotation=90)
st.pyplot(fig)

df2=df.drop(['Sexo'],axis=1)
st.markdown("## Grafico de datos de Solo Grupo Etario mostrando ambos Sexos")
st.sidebar.markdown("### Grafico 2")
Grupo = st.sidebar.select_slider("Grupo Etario",df2['Grupo de edad'].unique())
st.write("Opción seleccionada:", Grupo)
superfiltro2=df2[(df2["Grupo de edad"]==Grupo)]
fig2,ax = plt.subplots()
to_plot=superfiltro2.iloc[:,2:-1]
ax.plot(to_plot.T)
ax.set_title(Grupo)
ax.set_ylabel("Cantidad de hombres y mujeres por Rango Etario")
ax.set_xlabel("Fecha")
xs= np.arange(0,superfiltro2.shape[1]-2,30)
plt.xticks(xs,rotation=90)
st.pyplot(fig2)

df3=df.drop(['Grupo de edad'],axis=1)
df3=df3.groupby('Sexo').sum()
df3=df3.rename_axis('Sexo').reset_index()
st.markdown("## Grafico de datos de Solo Grupo Etario mostrando la suma de ambos Sexos")
st.sidebar.markdown("### Grafico 3")
Grupo2 = st.sidebar.radio("Sexo",df3.Sexo.unique())
st.write("Opción seleccionada:", Grupo2)
superfiltro3=df3[(df3.Sexo==Grupo2)]
fig3,ax = plt.subplots()
to_plot=superfiltro3.iloc[:,2:-1]
ax.plot(to_plot.T)
ax.set_title(Grupo2)
ax.set_ylabel("Cantidad total de hombres y mujeres por Sexo")
ax.set_xlabel("Fecha")
xs= np.arange(0,superfiltro3.shape[1]-2,30)
plt.xticks(xs,rotation=90)
st.pyplot(fig3)
