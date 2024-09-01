import pandas as pd

data = {
    "Duration": [60, 60, 60, 45, 45, 60, 60, 450, 30, 60, 60, 60, 60, 60, 60, 60, 60, 60, 45, 60, 45, 60, 45, 60, 45, 60, 60, 60, 60, 60, 60, 60],
    "Date": ['2020/12/01', '2020/12/02', '2020/12/03', '2020/12/04', '2020/12/05', '2020/12/06', '2020/12/07', '2020/12/08', '2020/12/09', '2020/12/10',
             '2020/12/11', '2020/12/12', '2020/12/12', '2020/12/13', '2020/12/14', '2020/12/15', '2020/12/16', '2020/12/17', '2020/12/18', '2020/12/19',
             '2020/12/20', '2020/12/21', None, '2020/12/23', '2020/12/24', '2020/12/25', '20201226', '2020/12/27', '2020/12/28', '2020/12/29', '2020/12/30', '2020/12/31'],
    "Pulse": [110, 117, 103, 109, 117, 102, 110, 104, 109, 98, 103, 100, 100, 106, 104, 98, 98, 100, 90, 103, 97, 108, 100, 130, 105, 102, 100, 92, 103, 100, 102, 92],
    "Maxpulse": [130, 145, 135, 175, 148, 127, 136, 134, 133, 124, 147, 120, 120, 128, 132, 123, 120, 120, 112, 123, 125, 131, 119, 101, 132, 126, 120, 118, 132, 132, 129, 115],
    "Calories": [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 374.0, 253.3, 195.1, 269.0, 329.3, 250.7, 250.7, 345.3, 379.3, 275.0, 215.2, 300.0, None, 323.0, 243.0, 364.2, 282.0, 300.0, 246.0, 334.5, 250.0, 241.0, None, 280.0, 380.3, 243.0]
}

df = pd.DataFrame(data)

# print(pd.to_datetime(df['Date']))
print(df["Date"])

#the thing is that to_datetime() assumes that the default format is YYYY-MM-DD, MM/DD/YYYY, etc.
#but in cases like 20201226 the format is YYYYMMDD
#that is why we use format to tell the to_datetime() that format are mixed
#all these things can be handled using errors='coerce' but in this case as we not just different type
#of format but also mixed format that's why we have to use format and errors both otherwise
#it would have been completed by errors only, because errors = 'coerce' can handle different default formats
#but not mixed format
df["Date"] = pd.to_datetime(df["Date"],format='mixed',errors='coerce')
print(df["Date"])

df.dropna(subset="Date", inplace=True)

print(df["Date"])