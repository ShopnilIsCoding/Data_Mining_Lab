import pandas as pd
from sklearn.preprocessing import minmax_scale
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
#Task->1
df=pd.read_csv("student_performance.csv")

print(df.head())

print("Summarizing the data types and missing values:")
print(df.dtypes)
print(df.isnull().sum())

#Task->2
print("Replacing missing value in 'Study_Hours' and 'Attendance(%)' with mean:")
df['Study_Hours'].fillna(df['Study_Hours'].mean(), inplace=True)
df['Attendance(%)'].fillna(df['Attendance(%)'].mean(), inplace=True)
print("Missing values after replacement:")
print(df.isnull().sum())

#Task->3
print("Data Before normalization:")
print(df[['Study_Hours', 'Test_Score']].head())
df_cpy=df.copy()
df_cpy['Study_Hours'] = minmax_scale(df_cpy['Study_Hours'])
df_cpy["Test_Score"] = minmax_scale(df_cpy["Test_Score"])
print("Data after normalization:")
print(df_cpy[['Study_Hours', 'Test_Score']].head())

#Task->4

sorted_ages = sorted(df['Age'])
bin_size = 3
bins = list(range(int(min(sorted_ages)), int(max(sorted_ages)) + bin_size + 1, bin_size))
labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins)-1)]
df['Age_Bin'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
print("Data after discretization:")
print(df[['Age', 'Age_Bin']])

print("replacing each value with nearest boundary value:")

for index, row in df.iterrows():
    age = row['Age']
    lower, upper = map(int, row['Age_Bin'].split('-'))

    if abs(age - lower) <= abs(age - upper):
        df.loc[index, 'Age'] = lower
    else:
        df.loc[index, 'Age'] = upper

print(df[['Age','Age_Bin']])
#Task->5

print("Converting Gender and Grade into numerical format using label encoding:")

# label_encoder = LabelEncoder()
df['Gender'] = pd.get_dummies(df['Gender'], drop_first=True)

df['Grade'] = df['Grade'].map({'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0})

print("Data after encoding:")
print(df[['Gender', 'Grade']].head())

#Task->6

def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

print("Detecting outliers in 'Study_Hours':")
outliers_study_hours = detect_outliers(df, 'Study_Hours')
print(outliers_study_hours['Study_Hours'])

#Task->7

cleaned_df = df.drop(columns=['Student_ID'])
print("Data after dropping 'Student_ID':")
print(cleaned_df.head())