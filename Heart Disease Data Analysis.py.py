# -*- coding: utf-8 -*-
"""Heart disease data

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QMEmJbFp0PpNpgcV468JSbrVItyHe4xR

NAME: Gaurav Mahajan

Project Title: Heart Disease Analysis
Problem Statement: Health is real wealth in the pandemic time we all realized the brute effects of covid-19 on all irrespective of any status.You are required to analyze this health and medical data for better future preparation.

 Do ETL: Extract- Transform and Load data from the heart disease diagnostic database
 You can perform EDA through python. The database extracts various information such as
 Heart disease rates, Heart disease by gender, by age.
 You can even compare attributes of the data set to extract necessary information. Make the
 necessary dashboard with the best you can extract from the data. Use various visualization
 and features and make the best dashboard
 Find key metrics and factors and show the meaningful relationships between attributes.
 Do your own research and come up with your findings.

1. ETL (Extract , Transform, Load) process
2. Exploratory Data Analysis(EDA)
3. Data Visualization
4. Feature Engineering
5. Model Building
6. Evaluation And Interpretation

### ETL (Extract , Transform, Load) **Process**

Step 1: Import Necessary Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

Step 2: Load the Dataset

#load the dataset
df = pd.read_csv('/Heart Disease data.csv')

Step 3: Initial data inspection

# display the first few rows of the dataframe
print(df.head())

#check for missing values
print(df.isnull().sum())

#check the data types of each column
print(df.describe())

Step 4: Display Top 5 rows of the dataset

print (df.head())

print (df.tail())

"""Step 6:find shape of our dataset (number of rows and columns)."""

print(f"shape of the dataset: {df.shape}")

print(df.info())

print(df.isnull().sum())

"""Step 9: Check for Duplicate Data and Drop Them."""

#Check for Duplicates
duplicate_rows = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_rows}")

#Drop duplicates
df = df.drop_duplicates()
print(f"Shape of thr dataset after dropping duplicates: {df.shape}")

"""Step 10: Get overall statistics About the dataset

"""

print(df.describe())

"""Step 10: how many people have heart disesase , and How many Don't have Heart Disease in this dataset?"""

heart_disease_count = df['target'].value_counts()
print(heart_disease_count)

gender_count = df['sex'].value_counts()
print(gender_count)

"""# Exploratory Data Analysis(EDA)**bold text**"""

#Step 1: Understand the distribution of the data

#plot histogram for all numeric columns
df.hist(figsize=(10,10))
plt.show()

"""Step 2: Analyze the correlation between Variables"""

#craete a correlation matrix
Corr_matrix = df.corr()
# plot the hearmap
plt.figure(figsize=(10,10))
sns.heatmap(Corr_matrix, annot=True,cmap='coolwarm')
plt.show()

"""#3. Data Visualization"""

#step 1: Visualize heart disease rates by gender and age

#heart disease by gender
sns.countplot(x='sex', hue='sex', data=df)
plt.title('Heart Disease by Gender')
plt.show()

#heart disease by age
plt.figure(figsize=(10,6))
sns.histplot(df[df['target']==1]['age'],kde=True, color='red', label='Heart Disease')
sns.histplot(df[df['target']==0]['age'], kde=True, color='blue', label='No Heart Disease')
plt.legend()
plt.title('Heart Disease by Age')
plt.show()

Step 2: Check chest pain Type

chest_pain_count = df['cp'].value_counts()
print(chest_pain_count)

#show the chest pain distribuation as per target variable
sns.countplot(x='cp', hue='target', data=df)
plt.title('Chest Pain Distribution')
plt.show()

#Show fasting blood sugar distribution Accroding to target varibale
sns.countplot(x='fbs', hue='target', data=df)
plt.title('Fasting Blood Sugar Distribution')
plt.show()

#check resting blood pressure distribuation
plt.figure(figsize=(10,6))
sns.histplot(df[df['target']==1]['trestbps'], kde=True, color='red', label='Heart Disease')
plt.title('Resting Blood Pressure Distribution')
plt.show()

#compare resting blood pressure as per sex column
plt.figure(figsize=(10,6))
sns.boxplot(x='sex', y='trestbps', data=df)
plt.title('Resting Blood Pressure Distribution')
plt.show()

#show Distribuation of serum cholestrol
plt.figure(figsize=(10,6))
sns.histplot(df[df['target']==1]['chol'], kde=True, color='red', label='Heart Disease')
plt.title('Serum Cholestrol Distribution')
plt.show()

"""#4. Feature Engineering"""

step. 1 freature scaling

#split the data into features and target
x=df.drop('target', axis=1)
y=df['target']

#scale the features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

"""#5. Model Building"""

#step 1: split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

#step 2: train a logistic regression model
model = LogisticRegression()
model.fit(x_train, y_train)

"""#6 Evaluation and Interpretation"""

#step 1: make prediction and evaluate the model

#make predictions
y_pred = model.predict(x_test)

#evaluate the model
print("classification_report :\n",classification_report(y_test, y_pred))
print("confusion_matrix :\n",confusion_matrix(y_test, y_pred))
print("accuracy_score:\n",accuracy_score(y_test, y_pred))

#continous variables
Continuous_variables = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

#plot histograms for continous variables
plt.figure(figsize=(10,6))
for i, variable in enumerate(Continuous_variables):
  plt.subplot(2,3,i+1)
  sns.histplot(df[df['target']==1][variable], kde=True, color='red', label='Heart Disease')
plt.tight_layout()
plt.show()
