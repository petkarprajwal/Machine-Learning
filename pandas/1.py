import pandas as pd 

data={"Name":["John","Peter","anu"],
      "Age":[10,20,30],
      "Salary":[3000,4500,5600]}
df=pd.DataFrame(data)
#print(df)

data1=pd.read_excel("erp.xlsx", sheet_name="Sheet1")
#print(data1)

data2=pd.read_csv("Breast_cancer_dataset.csv")#download it from https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data
#print(data2)
#print(data2.head(15))  //to see the first 15 rows
#print(data2.tail(10))  //to see the last 10 rows
#print(data2.info())    //to get information about the dataset
#print(data2.describe())  //to get statistical summary of the dataset
#print(data2.isnull())   //to check for null values in the dataset
print(data2.isnull().sum())  