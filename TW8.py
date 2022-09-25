import pandas as pd
import numpy as np

myData = pd.read_csv("TW8t.csv")
print(myData.to_string())
print(".....table columns......")
print("===============================")
for col in myData.columns:
	print(col+"\t\t",end="")

colName = input("Enter col name: ")
print(myData.loc[0:10,colName].unique())
print(myData.groupby(colName)[colName].count())
print("Total rows in DFrame: "+str(myData.shape[0]))


# INSERT THIS IN CSV FILE:
# model,mpg,cyl,disp,hp,drat,wt,qsec,vs,am,gear,carb
# Mazda RX4,21,6,160,110,3.9,2.62,16.46,0,1,4,4
# Mazda RX4 Wag,21,6,160,110,3.9,2.875,17.02,0,1,4,4
# Datsun 710,22.8,4,108,93,3.85,2.32,18.61,1,1,4,1
# Hornet 4 Drive,21.4,6,258,110,3.08,3.215,19.44,1,0,3,1
# Hornet Sportabout,18.7,8,360,175,3.15,3.44,17.02,0,0,3,2
# Valiant,18.1,6,225,105,2.76,3.46,20.22,1,0,3,1
# Duster 360,14.3,8,360,245,3.21,3.57,15.84,0,0,3,4
# Merc 240D,24.4,4,146.7,62,3.69,3.19,20,1,0,4,2
# Merc 230,22.8,4,140.8,95,3.92,3.15,22.9,1,0,4,2
# Merc 280,19.2,6,167.6,123,3.92,3.44,18.3,1,0,4,4
# 
# THIS IS THE OUTPUT
#                model   mpg  cyl   disp   hp  ...   qsec  vs  am  gear  carb
# 0          Mazda RX4  21.0    6  160.0  110  ...  16.46   0   1     4     4
# 1      Mazda RX4 Wag  21.0    6  160.0  110  ...  17.02   0   1     4     4
# 2         Datsun 710  22.8    4  108.0   93  ...  18.61   1   1     4     1
# 3     Hornet 4 Drive  21.4    6  258.0  110  ...  19.44   1   0     3     1
# 4  Hornet Sportabout  18.7    8  360.0  175  ...  17.02   0   0     3     2
# 5            Valiant  18.1    6  225.0  105  ...  20.22   1   0     3     1
# 6         Duster 360  14.3    8  360.0  245  ...  15.84   0   0     3     4
# 7          Merc 240D  24.4    4  146.7   62  ...  20.00   1   0     4     2
# 8           Merc 230  22.8    4  140.8   95  ...  22.90   1   0     4     2
# 9           Merc 280  19.2    6  167.6  123  ...  18.30   1   0     4     4
# 
# [10 rows x 12 columns]
# Column names are:
# model
# mpg
# cyl
# disp
# hp
# drat
# wt
# qsec
# vs
# am
# gear
# carb
# Enter the attribute: mpg
# Unique Values for thr attribute are:  mpg are :
# 14.3
# 18.1
# 18.7
# 19.2
# 21.0
# 21.4
# 22.8
# 24.4
# Frequency of occurence of the unique values is :
# 14.3     1
# 18.1     1
# 18.7     1
# 19.2     1
# 21.0     2
# 21.4     1
# 22.8     2
# 24.4     1
# Total no of records:  10
# 
# Process finished with exit code 0