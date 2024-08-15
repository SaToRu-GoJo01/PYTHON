import pandas as pd

#VIEWING THE DATA
# One of the most used method for getting a quick overview of the DataFrame, is the head() method.

# The head() method returns the headers and a specified number of rows, starting from the top.

df = pd.read_csv('Pandas/data.csv')

print(df.head(10))
# Note: if the number of rows is not specified, the head() method will return the top 5 rows.


# Print the last 5 rows of the DataFrame:
print(df.tail(10))




#INFO ABOUT DATA

print(df.info())