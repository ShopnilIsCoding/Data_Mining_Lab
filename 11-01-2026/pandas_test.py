import pandas as pd
import numpy as np

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
data2 = pd.read_csv(
    r"E:\bubt\Data Mining Lab\11-01-2026\NUSW-NB15_features.csv",
    encoding="latin1"
)
print(data2)


#reading json file
data3 = pd.read_json(
    r"E:\bubt\Data Mining Lab\11-01-2026\fakeData.json")
print(data3.to_string())

#writing to csv file
data3.to_csv(
    r"E:\bubt\Data Mining Lab\11-01-2026\output.csv",
    index=False
)   
#writing to json file
data3.to_json(
    r"E:\bubt\Data Mining Lab\11-01-2026\output.json"
)
#data cleaning
data4 = {
  "A": [1, 2, None],
  "B": [None, 2, 3],
    "C": [1, None, 3]
}
df2 = pd.DataFrame(data4)
print(df2)
print(df2.isnull())

print(df2.dropna())
print(df2.fillna(0))
print(df2.fillna({"A": 0, "B": 1, "C": 2}))
print(df2.interpolate())
print(df2.replace(np.nan, 0, regex=False))
print(df2.drop_duplicates())
print(df2.astype(float))
print(df2.rename(columns={"A": "Alpha", "B": "Beta", "C": "Gamma"}))
print(df2.sample(frac=1))
print(df2.sample(n=2))
print(df2.sort_index())
print(df2.sort_values(by='A'))
print(df2.apply(lambda x: x * 2))
print(df2.map(lambda x: x * 2 if pd.notnull(x) else x))
print(df2.where(df2 > 1))

#merging dataframes
data5 = {
  "key": ["K0", "K1", "K2", "K3"],
  "A": ["A0", "A1", "A2", "A3"],
  "B": ["B0", "B1", "B2", "B3"]
}
data6 = {
  "key": ["K0", "K1", "K2", "K3"],
  "C": ["C0", "C1", "C2", "C3"],
  "D": ["D0", "D1", "D2", "D3"]
}
df3 = pd.DataFrame(data5)
df4 = pd.DataFrame(data6)
merged_df = pd.merge(df3, df4, on="key")
print(merged_df)
#concatenating dataframes
concatenated_df = pd.concat([df3, df4], axis=0)
print(concatenated_df)
#joining dataframes
joined_df = df3.set_index('key').join(df4.set_index('key'))
print(joined_df)

#pivoting dataframe
data7 = {
  "A": ["foo", "bar", "foo", "bar"],
  "B": ["one", "one", "two", "two"],
  "C": [1, 2, 3, 4]
}
df5 = pd.DataFrame(data7)
pivoted_df = df5.pivot(index='A', columns='B', values='C')
print(pivoted_df)

#correlation between two columns

df = pd.DataFrame({
    "height": [160, 170, 180, 190],
    "weight": [60, 72, 80, 90]
})

corr = df["height"].corr(df["weight"])
print(corr)
print(concatenated_df)
cleaned_df = concatenated_df.dropna( subset=["A"], inplace=True)
print(cleaned_df)