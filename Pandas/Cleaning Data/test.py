import pandas as pd
s = pd.Series(['10', '12', '15', '20', 'A', '31', 'C', 'D'])
# pd.to_numeric(s,errors="coerce")
pd.to_numeric(s, errors='coerce')
print(s.info())