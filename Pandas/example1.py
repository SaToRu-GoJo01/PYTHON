import pandas as pd

myDataSet = {
    'Cars' : ["BMW","Volvo","Ford"],
    'passings' : [3,7,2]
}

print(myDataSet)

my_var = pd.DataFrame(myDataSet)

print(my_var)

print(pd.__version__)