print("hellow data science")

mylist = [1, 2, 3, 4, 5]
for item in mylist:
    print("mylist: ",item)

for i in range(3):
    print("Iteration:", i)


mydict = {'a': 1, 'b': 2, 'c': 3}
for key, value in mydict.items():
    print(f"key: {key}, value: {value}")

num = 15
if num > 10:
    print(num, "is greater than 10")
elif num == 10:
    print(num, "is equal to 10")
else:
    print(num, "is less than 10")

import pandas as pd
result = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("Pandas Series:\n", result)

import pandas as pd

#df = pd.read_csv('D:\Chan\Learning\data.csv')
#print("CTRU data:\n", df.head(25))
import os
print(os.path.exists("data.csv"))