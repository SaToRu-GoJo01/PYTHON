import re

txt = "The rain in Spain is good"
x = re.findall("^The.*Spain.", txt)

print(x)

print(txt,1)

x = re.sub("^The.*Spain$"," Hello ",txt)

print(x,txt,2)