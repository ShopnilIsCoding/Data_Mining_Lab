import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv('student_preprocessing_dataset.csv')
print(df)

# print("\n total missing values:")
# print(df.isnull().sum())

# print("\n mean of age column:")
# print(df["Age"].mean())

df["Age"].fillna(df["Age"].mean(), inplace=True)
# print("\n total missing values after filling in Age:")
# print(df.head())

#categorical data-> mode 
#numerical data-> mean,median

# df["Gender"].fillna(df["Gender"].mode()[0], inplace=True)
# print("\n total missing values after filling in Gender:")
# print(df.tail())


# topic 2->duplicate values

# print("\n total duplicate values:")
# print(df.duplicated().sum())

# df.drop_duplicates(inplace=True)
# print("\n total duplicate values after dropping duplicates:")
# print(df.duplicated())
# print(df)

# topic 3->datatype check
# print("\n data types of each column:")
# print(df.dtypes)
# # df["Attendance"]=df["Attendance"].astype(float)
# # print("\n data types of each column after converting Attendance to float:") 
# # print(df.dtypes)
# df["Attendance"]=pd.to_numeric(df["Attendance"], errors='coerce')
# print("\n data types of each column after converting Attendance to numeric:")
# print(df)

# plt.figure(figsize=(10,6))
# plt.boxplot(df["Age"])
# plt.title("Box plot of Age")
# plt.xlabel("Age")
# plt.ylabel("Values")
# plt.grid(True)

# def detect_outliers_iqr(data,column):
#     Q1 = data[column].quantile(0.25)
#     Q3 = data[column].quantile(0.75)
#     IQR = Q3 - Q1
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
#     outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
#     return outliers

# def remove_outliers_iqr(data,column):
#     Q1 = data[column].quantile(0.25)
#     Q3 = data[column].quantile(0.75)
#     IQR = Q3 - Q1
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
#     outliers = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
#     return outliers


# print("\n outliers in Age column:")
# print(detect_outliers_iqr(df,"Age"))

# print("\n Age column after removing outliers:")
# print(remove_outliers_iqr(df,"Age"))



# outlier using z-score

# def detect_outliers_zscore(data, column):
#     mean = data[column].mean()
#     std = data[column].std()
    
#     z_scores = (data[column] - mean) / std
    
#     outliers = data[np.abs(z_scores) > 3]
#     return outliers

# detect_outliers_zscore(df, "Marks")
# print("\n outliers in Marks column:")
# print(detect_outliers_zscore(df, "Marks"))

# def remove_outliers_zscore(data, column):
#     mean = data[column].mean()
#     std = data[column].std()
    
#     z_scores = (data[column] - mean) / std
    
#     clean_data = data[np.abs(z_scores) <= 3]
#     return clean_data
 
# print("\n Marks column after removing outliers:")
# print(remove_outliers_zscore(df, "Marks"))

# topic 4->encoding 

# df["Gender_Encoded"]=df["Gender"].map({"Male":0,"Female":1})

# print("\n dataset after encoding Gender column:")
# print(df)

# df=pd.get_dummies(df, columns=["Department"], prefix="Dept")
# print("\n dataset after one-hot encoding Department column:")
# print(df)


# from sklearn.preprocessing import LabelEncoder

# le = LabelEncoder()
# df["Gender_encoded"] = le.fit_transform(df["Gender"].astype(str))
# print("\n dataset after label encoding Gender column:")
# print(df)   


# topic 5->scaling
df_min_max_scaled = df.copy()
df_min_max_scaled["Marks"] = (df["Marks"] - df["Marks"].min()) / (df["Marks"].max() - df["Marks"].min())
print("\n dataset after min-max scaling Marks column:")
print(df_min_max_scaled)

from sklearn.preprocessing import MinMaxScaler
df_scaled = df.copy()
df_scaled["Marks"] = MinMaxScaler().fit_transform(df[["Marks"]])
print("\n dataset after min-max scaling Marks column using sklearn:")
print(df_scaled)


