import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

day_df = pd.read_csv("day.csv")#--> Menambahkan file day.csv
hour_df = pd.read_csv("hour.csv")#--> menambahkan file hour.csv

datetime_columns = ["dteday"]
     
for column in datetime_columns:
    day_df[column] = pd.to_datetime(day_df[column]) #--> mengganti tipe data dteday dari object ke datetime pada day.csv
    hour_df[column] = pd.to_datetime(hour_df[column]) #--> mengganti tipe data dteday dari object ke datetime pada hour.csv


st.header('Bike Sharing Dataset :sparkles:')#--> Memberikan header/judul pada websie


col1, col2, col3 = st.columns(3)#--> Membuat 3 kolom pada website

cnt = day_df.cnt.sum()
col1.metric("Total penyewaan", value=cnt) #--> kolom pertama berisi total penyewaan
casual = day_df.casual.sum()
col2.metric("Total Penyewa kasual", value=casual) #--> kolom kedua berisi total penyewa kasual
registered = day_df.registered.sum()
col3.metric("total Penyewa berlangganan", value=registered) #--> kolom ketiga berisi total penyewa berlangganan


st.subheader('Jumlah Penyewaan sepeda beberapa bulan/tahun terakhir: ')#--> Menambah subheader/subjudul pada website untuk plot pertama

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    day_df["dteday"], day_df["cnt"], color='red'
)#--> Menambahkan plot untuk menampilkan total penyewa setiap bulan/tahun

st.pyplot(fig)


st.text('\n')


st.subheader('Jumlah penyewaan berdasarkan cuaca: ')#--> Menambah subheader/subjudul pada website untuk plot kedua

st.text("""
1: Clear, Few clouds, Partly cloudy, Partly cloudy
2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
""")#--> Menambahkan text untuk keterangan plot diatas

fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(day_df, x="weathersit", y="cnt", errorbar=None)#--> Menambahkan plot untuk menampilkan penyewa berdasarkan cuaca
st.pyplot(fig)


st.text('\n')


st.subheader("Penyewaan Rata-rata Jam perhari: ")#--> Menambah subheader/subjudul pada website untuk plot ketiga

day_hour_df = pd.merge(
    day_df,
    hour_df,
    on='dteday'
)#--> Menggabungkan day_df % hour_df, menjadi df baru(day_hour_df)

rata_jam_df = day_hour_df.groupby('dteday')['hr'].mean().reset_index()#--> membuat df baru(rata_jam_df) untuk menyimpan data rata-rata jam perhari

hr = rata_jam_df.hr.sum()
st.metric("total rata-rata jam perhari", value=hr)#--> menampilkan informasi berapa rata-rata jam perhari

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    rata_jam_df['dteday'], 
    rata_jam_df['hr'], 
    color='red'
)#--> Menambahkan plot untuk menampilkan rata-rata jam perhari
st.pyplot(fig)