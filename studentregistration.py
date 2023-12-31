# -*- coding: utf-8 -*-
"""studentRegistration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fQL5UQKmPa382jEpMEl5YaxKOg6rHelt
"""

import pandas as pd

studentRegistration_data = pd.read_csv('studentRegistration.csv')

print(studentRegistration_data.head())
print(studentRegistration_data.info())
print(studentRegistration_data.describe())

print(studentRegistration_data.isnull().sum())

# Menghitung nilai rata-rata dari kolom 'date_registration'
mean_date_registration = studentRegistration_data['date_registration'].mean()

# Mengisi nilai-nilai yang hilang dengan nilai rata-rata
studentRegistration_data['date_registration'].fillna(mean_date_registration, inplace=True)

# Tampilkan data setelah pengisian nilai-nilai yang hilang
print(studentRegistration_data.head())

print(studentRegistration_data.isnull().sum())

# Menghitung nilai rata-rata dari kolom 'date_unregistration'
mean_date_unregistration = studentRegistration_data['date_unregistration'].mean()

# Mengisi nilai-nilai yang hilang dengan nilai rata-rata
studentRegistration_data['date_unregistration'].fillna(mean_date_unregistration, inplace=True)

# Tampilkan data setelah pengisian nilai-nilai yang hilang
print(studentRegistration_data.head())

print(studentRegistration_data.isnull().sum())

import matplotlib.pyplot as plt

# Visualisasi data
plt.figure(figsize=(10, 6))
plt.hist(studentRegistration_data['date_unregistration'], bins=50, color='skyblue', edgecolor='black')
plt.title('Distribusi Tanggal Unregistration')
plt.xlabel('Tanggal Unregistration')
plt.ylabel('Jumlah Mahasiswa')
plt.show()

import seaborn as sns

# Analisis distribusi
mean = studentRegistration_data['date_unregistration'].mean()
median = studentRegistration_data['date_unregistration'].median()
std_deviation = studentRegistration_data['date_unregistration'].std()
skewness = studentRegistration_data['date_unregistration'].skew()
kurtosis = studentRegistration_data['date_unregistration'].kurtosis()

# Tampilkan informasi statistik
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_deviation}")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurtosis}")

# Visualisasi distribusi
plt.figure(figsize=(10, 6))
sns.histplot(studentRegistration_data['date_unregistration'], kde=True, color='skyblue')
plt.title('Distribusi Tanggal Unregistration')
plt.xlabel('Tanggal Unregistration')
plt.ylabel('Frekuensi')
plt.show()

# Analisis korelasi antara 'date_registration' dan 'date_unregistration'
correlation = studentRegistration_data['date_registration'].corr(studentRegistration_data['date_unregistration'])

# Visualisasi korelasi dengan heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(studentRegistration_data[['date_registration', 'date_unregistration']].corr(), annot=True, cmap='coolwarm')
plt.title('Korelasi antara Date Registration dan Date Unregistration')
plt.show()

# Tampilkan nilai korelasi
print(f"Korelasi antara Date Registration dan Date Unregistration: {correlation:.2f}")

# Ubah kolom 'date_registration' dan 'date_unregistration' menjadi tipe data datetime
studentRegistration_data['date_registration'] = pd.to_datetime(studentRegistration_data['date_registration'])
studentRegistration_data['date_unregistration'] = pd.to_datetime(studentRegistration_data['date_unregistration'])

# Ekstrak tahun dan semester dari tanggal pendaftaran
studentRegistration_data['registration_year'] = studentRegistration_data['date_registration'].dt.year
studentRegistration_data['registration_semester'] = studentRegistration_data['date_registration'].dt.month // 6 + 1

# Analisis pola pendaftaran per tahun
registration_by_year = studentRegistration_data.groupby('registration_year').size()
registration_by_year.plot(kind='bar')
plt.title('Jumlah Pendaftaran per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Pendaftaran')
plt.show()

# Analisis pola pendaftaran per semester
registration_by_semester = studentRegistration_data.groupby('registration_semester').size()
registration_by_semester.plot(kind='bar')
plt.title('Jumlah Pendaftaran per Semester')
plt.xlabel('Semester')
plt.ylabel('Jumlah Pendaftaran')
plt.show()

# Analisis pola pembatalan per tahun
unregistration_by_year = studentRegistration_data.groupby(studentRegistration_data['date_unregistration'].dt.year).size()
unregistration_by_year.plot(kind='bar')
plt.title('Jumlah Pembatalan per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Pembatalan')
plt.show()

# Analisis pola pembatalan per semester
unregistration_by_semester = studentRegistration_data.groupby(studentRegistration_data['date_unregistration'].dt.month // 6 + 1).size()
unregistration_by_semester.plot(kind='bar')
plt.title('Jumlah Pembatalan per Semester')
plt.xlabel('Semester')
plt.ylabel('Jumlah Pembatalan')
plt.show()

