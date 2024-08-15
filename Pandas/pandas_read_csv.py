import pandas as pd

df = pd.read_csv('Pandas/data.csv')

print(df)
#use .to_string() to print entire dataframe
print(df.to_string())
#or change the default max printing value with pd.options.display.max_rows
print(pd.options.display.max_rows)
# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

pd.options.display.max_rows = 9999

print(df)