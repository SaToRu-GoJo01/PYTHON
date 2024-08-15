import pandas as pd

a = [1,7,2]

my_var = pd.Series(a)

print(my_var)

print(my_var[0])

print(my_var.name)

my_var = pd.Series(a,index = ["x","y","z"])

print(my_var)

print(my_var["z"])


#Key and value pair with series
#Note: The keys of the dictionary become the labels.

calories = {"Day1":420,"Day2":380,"Day3":390}

my_var = pd.Series(calories)

print(my_var)

#To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

my_var = pd.Series(calories,index = ["Day1","Day2"])

print(my_var)


#dataFrames using two series

data = {
    "calories":[420,380,390],
    "duration":[50,40,45]
}

my_var = pd.DataFrame(data)

print(my_var)