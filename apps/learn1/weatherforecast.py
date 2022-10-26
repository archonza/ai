import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O

#Load the csv file as data frame
df = pd.read_csv("C:/Dev/Ai/learn1/weatherAUS.csv")

#Data preprocessing
df = df.drop(columns=['Sunshine','Evaporation','Cloud3pm','Cloud9am','Location','Rainfall','Date'], axis=1)
print(df.shape)

# Display the data

print(df.count().sort_values())
print("Size of weather data frame is: ", df.shape)

df = df.dropna(how='any')
print(df.shape)
from scipy import stats
z = np.abs(stats.zscore(df._get_numeric_data()))
print(z)
df = df[(z < 3).all(axis=1)]
print(df.shape)
df['RainToday'].replace({'No': 0,'Yes': 1},inplace=True)
df['RainTomorrow'].replace({'No': 0,'Yes': 1},inplace=True)