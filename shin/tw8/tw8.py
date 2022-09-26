import pandas as pd 
import numpy as np

data = pd.read_csv("tw8.csv")
print(data)

cols=list(data.columns)
print("______table columns______")
print("=========================")
for col in cols:
    print(col)
    
attr=input("Enter the attribute")
attrvals = list(data[attr])

uniq = np.unique(attrvals)
print("Unique values for the attribute are:",attr,"are:")
  
for u in uniq:
    print(u)
    
print("Frequency of occurence of the unique values is:")

for u in uniq:
    print(u,' ',attrvals.count(u))
    
print("Total no of records :",len(data))
    