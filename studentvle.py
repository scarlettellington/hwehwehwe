# -*- coding: utf-8 -*-
"""studentVle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bZdaN43kIDIIIgTtMWVZL95PapGGkR3b
"""

import pandas as pd

studentVle_data = pd.read_csv('studentVle.csv')

print(studentVle_data.head())
print(studentVle_data.info())
print(studentVle_data.describe())

print(studentVle_data.isnull().sum())

studentVle_data['id_student'].fillna(studentVle_data['id_student'].mean(), inplace=True)
studentVle_data['id_site'].fillna(studentVle_data['id_site'].mean(), inplace=True)
studentVle_data['date'].fillna(studentVle_data['date'].mean(), inplace=True)
studentVle_data['sum_click'].fillna(studentVle_data['sum_click'].mean(), inplace=True)
print(studentVle_data.isnull().sum())

# Mengambil kolom-kolom numerik
numeric_columns = studentVle_data.select_dtypes(include=['number'])

# Menghitung statistik deskriptif
descriptive_stats = numeric_columns.describe()

# Menampilkan hasil statistik deskriptif
print(descriptive_stats)

import matplotlib.pyplot as plt

# Visualisasi Histogram untuk kolom 'sum_click'
plt.hist(studentVle_data['sum_click'], bins=20, color='blue', alpha=0.7)
plt.title('Histogram of sum_click')
plt.xlabel('sum_click')
plt.ylabel('Frequency')
plt.show()

# Visualisasi Scatter Plot antara 'sum_click' dan 'date'
plt.scatter(studentVle_data['date'], studentVle_data['sum_click'], color='red', alpha=0.5)
plt.title('Scatter Plot of sum_click vs. date')
plt.xlabel('date')
plt.ylabel('sum_click')
plt.show()

# Hitung korelasi antara variabel numerik
correlation_matrix = studentVle_data.corr()
print(correlation_matrix)

print(studentVle_data.columns)

# Jika ada kolom waktu, Anda dapat melakukan analisis waktu
# Misalnya, untuk mengecek tren harian dalam 'sum_click'
studentVle_data['date'] = pd.to_datetime(studentVle_data['date'])
daily_sum_click = studentVle_data.groupby(studentVle_data['date'].dt.date)['sum_click'].sum()
daily_sum_click.plot(title='Daily sum_click Trend')
plt.xlabel('Date')
plt.ylabel('sum_click')
plt.show()

# Temukan outlier menggunakan metode IQR (Interquartile Range)
Q1 = studentVle_data['sum_click'].quantile(0.25)
Q3 = studentVle_data['sum_click'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = studentVle_data[(studentVle_data['sum_click'] < lower_bound) | (studentVle_data['sum_click'] > upper_bound)]
print("Outliers:")
print(outliers)

