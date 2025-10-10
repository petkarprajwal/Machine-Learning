import pandas as pd 

df=pd.read_csv('weather.csv')
#print(df)
#print(df['MaxTemp'].max())
#df['MaxTemp'].plot()
#print(df["WindGustDir"][df["RainToday"]=="Yes"][df["RainTomorrow"]=="Yes"])
#print(df["Evaporation"].mean())

df1=pd.read_csv('weather data missing values .csv')
#print(df1)

df1.fillna(0,inplace=True)
#print(df1)
print(df1["Evaporation"].mean())