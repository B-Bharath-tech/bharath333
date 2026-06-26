from numpy import median
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

print("understanding dataset")
file_name='sales_data.csv'
if not os.path.exists(file_name):
    print(f"error {file_name} file not found")
    exit()

df=pd.read_csv(file_name)
print("successfully loaded")
print(f"shape of the dataset {df.shape[0]},Columns:{df.shape[1]}")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print("handling Misssing Values")
print(df.isnull().sum())
median_age=df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)
print(median_age)

median_Spending=df['Spending'].median()
df['Spending'] = df['Spending'].fillna(median_Spending)
print(median_Spending)

mean_Spending=df['Spending'].mean()
df['Spending'] = df['Spending'].fillna(mean_Spending)
print(mean_Spending)


mean_age=df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)
print(mean_age)

#distribution Analysis
plt.figure(figsize=(7,4))
df['Spending'].hist(bins=10,color='skyblue',edgecolor='black')
plt.title('Distribution of Spending')
plt.xlabel('Spending Amount')
plt.ylabel("number of customers")
plt.show()

#coorelation matrix
correlation =df.corr(numeric_only=True)
print(correlation)

print("PLotting Correlation Heeatmap")
plt.figure(figsize=(7,4))
sns.heatmap(correlation,annot=True ,cmap='coolwarm',fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

print("Find the Outliner in Age")
outliner=df[df['Age']>100]
print("Found Outliner(s):")
print(outliner)