import pandas as pd
path="data/automobile.csv"
df=pd.read_csv(path)

#Gives the stat info of the table eg mean , median , standard deviation
#print(df.describe(include="all"))

print(df.info)
