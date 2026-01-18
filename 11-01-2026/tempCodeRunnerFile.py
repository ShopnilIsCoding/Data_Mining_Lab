import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

#pandas series
a = [1, 7, 2]
myvar2 = pd.Series(a, index = ["x", "y", "z"])
print(myvar2)

#data frame from series
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.iloc[0])
print(df['calories'])
print(df[['calories', 'duration']])
print(df.iloc[:, 0])
print(df.iloc[0:2, 0])
print(df.iloc[:, :1])
print(df.iloc[0:2, :])
print(df[df.calories > 400])
print(df[df.duration < 45])
print(df.reset_index())
print(df.set_index("duration"))
print(df.sort_values(by='calories'))
print(df.describe())
print(df.info())
print(df.head(2))
print(df.tail(2))
print(df.mean())
print(df.sum())
print(df.min())
print(df.max())
print(df.std())
print(df.var())
print(df.count())
print(df.corr())
print(df.groupby('calories').sum())
print(df.groupby('duration').mean())
print(df.to_numpy())

#reading csv file
data2 = pd.read_csv(r"E:\bubt\Data Mining Lab\11-01-2026\NUSW-NB15_features.csv")
print(data2)
