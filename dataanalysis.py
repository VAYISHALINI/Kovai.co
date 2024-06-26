# -*- coding: utf-8 -*-
"""DataAnalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S5tNMUZ6f7CoGrPsE26L_HxcsgWZ3HA-
"""

import pandas as pd

data=pd.read_csv('/content/sample_data/Daily_Public_Transport_Passenger_Boardings_By_Ticket_Type_20240513.csv')

df=pd.DataFrame(data)
df.head()

df.shape
df.describe()



df.isnull().sum()

df.dropna() #handle missing values

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['MyWay', 'Paper Ticket']])
df[['MyWay', 'Paper Ticket']] = scaled_features

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='MyWay', bins=10, kde=True, color='blue', label='MyWay')
sns.histplot(data=df, x='Paper Ticket', bins=10,  color='red', label='Paper Ticket')
plt.title('Distribution of Ticket Counts')
plt.xlabel('Ticket Counts')
plt.ylabel('Frequency')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['MyWay'], label='MyWay')
plt.plot(df.index, df['Paper Ticket'], label='Paper Ticket')
plt.title('Ticket Counts Over Time')
plt.xlabel('Date')
plt.ylabel('Ticket Counts')
plt.legend()
plt.show()

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Extracting month
df['Month'] = df['Date'].dt.month

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x=df['Month'], y='MyWay',  marker='o')
sns.lineplot(data=df, x=df['Month'], y='Paper Ticket',  marker='o')
plt.title('Ticket Counts Over Months')
plt.xlabel('Month')
plt.ylabel('Ticket Counts')
plt.legend(title='Year')
plt.show()

import matplotlib.pyplot as plt

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Date'], df['MyWay'], label='MyWay', marker='o')
plt.scatter(df['Date'], df['Paper Ticket'], label='Paper Ticket', marker='o')
plt.title('Ticket Counts Over Time')
plt.xlabel('Date')
plt.ylabel('Ticket Counts')
plt.legend()
plt.grid(True)
plt.show()

df['Year'] = df['Date'].dt.year

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x=df['Year'], y='MyWay',  marker='o')
sns.lineplot(data=df, x=df['Year'], y='Paper Ticket',  marker='o')
plt.title('Ticket Counts Over Years')
plt.xlabel('Year')
plt.ylabel('Ticket Counts')
plt.legend(title='Year')
plt.show()

# Assuming 'df' is the DataFrame containing the dataset
correlation = df['MyWay'].corr(df['Paper Ticket'])
print("Correlation between MyWay and Paper Ticket:", correlation)