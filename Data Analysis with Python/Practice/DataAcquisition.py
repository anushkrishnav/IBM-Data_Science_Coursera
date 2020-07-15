import pandas as pd
df=pd.read_csv("data/imports-85.csv",header=None)

#print top 5 rows
#print(df.head(5))

#Print bottom 5 rowa
#print(df.bottom(5))

#headers
headers=["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns=headers

#drop rows with missing value
df.dropna(subset=["price"],axis=0)
print(df.head(10))
df.to_csv("data/automobile.csv")
