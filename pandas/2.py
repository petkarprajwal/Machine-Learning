#Handle the missing data 
import pandas as pd 
data=pd.read_csv("missing_data_students.csv")
#print(data)
#print(data.duplicated()) // to check for duplicate rows
#print(data.drop_duplicates()) // to drop duplicate rows
#print(data.drop_duplicates()) #// to drop duplicate rows
#print(data["Name"].duplicated()) // to check for duplicate names and their sum
print(data["Name"].drop_duplicates())
#print(data)