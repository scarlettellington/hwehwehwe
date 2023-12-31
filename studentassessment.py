# -*- coding: utf-8 -*-
"""studentAssessment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xXNgRq9_C31zk9FXZrAxNE9O6NHOyKs4
"""

import pandas as pd

studentAssessment_data = pd.read_csv('studentAssessment.csv')

print(studentAssessment_data.head())
print(studentAssessment_data.info())
print(studentAssessment_data.describe())

print(studentAssessment_data.isnull().sum())

# Mengisi nilai yang hilang dengan nilai rata-rata
mean_score = studentAssessment_data['score'].mean()
studentAssessment_data['score'].fillna(mean_score, inplace=True)

print(studentAssessment_data.isnull().sum())
studentAssessment_data.to_csv("studentAssessment_filled.csv", index=False)

import pandas as pd
import matplotlib.pyplot as plt

# Memuat dataset yang telah diisi dengan nilai rata-rata
df = pd.read_csv("studentAssessment_filled.csv")

# Visualisasi distribusi skor
plt.figure(figsize=(8, 6))
plt.hist(df['score'], bins=20, edgecolor='k')
plt.title('Distribusi Skor')
plt.xlabel('Skor')
plt.ylabel('Jumlah Mahasiswa')
plt.show()

# Visualisasi jumlah mahasiswa berdasarkan status is_banked
plt.figure(figsize=(6, 4))
df['is_banked'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Jumlah Mahasiswa berdasarkan Status is_banked')
plt.xlabel('Status is_banked')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=0)
plt.show()

import seaborn as sns

# Memuat dataset yang telah diisi dengan nilai rata-rata
df = pd.read_csv("studentAssessment_filled.csv")

# Analisis pengaruh is_banked terhadap skor
sns.boxplot(data=df, x='is_banked', y='score')
plt.title('Pengaruh Status "is_banked" terhadap Skor')
plt.xlabel('Status is_banked')
plt.ylabel('Skor')
plt.show()