# -*- coding: utf-8 -*-
"""courses.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S7WvpTUWHHR-hitnFOJwikmCUkiw8iR-
"""

import pandas as pd

courses_data = pd.read_csv('courses.csv')

print(courses_data.head())
print(courses_data.info())
print(courses_data.describe())

print(courses_data.isnull().sum())

# Visualisasi data
import matplotlib.pyplot as plt

# Histogram untuk 'module_presentation_length'
plt.hist(courses_data['module_presentation_length'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('module_presentation_length')
plt.ylabel('Jumlah Kursus')
plt.title('Distribusi module_presentation_length')
plt.show()

# Menampilkan korelasi antara kolom numerik
correlation = courses_data.corr()
print("\nKorelasi antara kolom numerik:")
print(correlation)

# Analisis 1: Hubungan antara 'code_module' dan 'module_presentation_length'
mean_length_by_module = courses_data.groupby('code_module')['module_presentation_length'].mean()
print("Rata-rata panjang presentasi modul berdasarkan kode modul:")
print(mean_length_by_module)

# Analisis 2: Distribusi 'module_presentation_length' di seluruh 'code_presentation'
plt.figure(figsize=(10, 6))
plt.hist(courses_data['module_presentation_length'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('module_presentation_length')
plt.ylabel('Jumlah Kursus')
plt.title('Distribusi module_presentation_length')
plt.show()

# Analisis 3: Perbedaan dalam panjang presentasi modul antara tahun presentasi
mean_length_by_year = courses_data.groupby('code_presentation')['module_presentation_length'].mean()
print("\nRata-rata panjang presentasi modul berdasarkan tahun presentasi:")
print(mean_length_by_year)

# Analisis 4: Pola perubahan panjang presentasi modul sepanjang waktu
plt.figure(figsize=(10, 6))
plt.plot(courses_data['code_presentation'], courses_data['module_presentation_length'], marker='o', linestyle='-')
plt.xlabel('Tahun Presentasi')
plt.ylabel('module_presentation_length')
plt.title('Perubahan module_presentation_length dari tahun ke tahun')
plt.xticks(rotation=45)
plt.show()