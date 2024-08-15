# Create a simple Pandas DataFrame:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)


#LOCATE ROW

# Pandas use the loc attribute to return one or more specified row(s)
print(df.loc[0])
# Note: This example returns a Pandas Series.

print(df.loc[[0,2]])


#NAMED INDEXES
#With the index argument, you can name your own indexes

df = pd.DataFrame(data, index = ["Day1","Day2","Day3"])
print(df)
print(df.loc["Day3"])


#LOAD FILES INTO A DATAFRAMES
#Load a comma separated file (CSV file) into a DataFrame:

df = pd.read_csv('Pandas/sample.csv')

print(df)