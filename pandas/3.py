#working with the missing data 
import pandas as pd 
data=pd.read_csv("missing_data_students.csv")

#print(data.isnull())   // to find the list of the data which are null or not 
#print(data.isnull().sum())     //to find the how many(sum) of the null values in the each row 
#print(data.dropna())    // to eleminate the missing data 
import numpy as np
#print(data.replace(np.nan,"hi"))   // used to replace for the whole dataset
#print(data["Science_Score"].replace(np.nan,30))     //used to replace for the single attribute 
#print(data["Science_Score"].mean())  # to find the mean of the Science_Score column
#print(data.fillna(method="bfill"))  # to fill the missing values with the previous value in the column
#print(data.fillna(method="ffill"))  # to fill the missing values with the next value in the column

print(data)
print(data[])