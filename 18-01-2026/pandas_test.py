import pandas as pd
import matplotlib.pyplot as plt

# read csv file
df=pd.read_csv(r"E:\bubt\Data Mining Lab\18-01-2026\\Titanic-Dataset.csv",encoding="latin1")

# print(df.head(),"\n\n")

# task 1: Missing Value Handling
# The "Cabin" column contains a large number of missing values.
# Drop this column entirely from the dataset.
# Then:
# Fill missing values in the "Embarked" column with the most frequent value.

cleaned_df = df.drop(columns=["Cabin"],inplace=False)
print("printing missing values before handling\n",cleaned_df.isnull().sum(),"\n\n")
cleaned_df = cleaned_df.fillna({"Embarked": cleaned_df["Embarked"].mode()[0]})
print("cleaned",cleaned_df,"\n\n")

# task 2. Duplicate Value Removal
# Check for and remove any duplicate rows in the dataset.
print("duplicates found:",cleaned_df.duplicated().sum(),"\n\n")
print("duplicates",cleaned_df[cleaned_df.duplicated()],"\n\n")
no_duplicates_df = cleaned_df.drop_duplicates()
print("after duplicate removal",no_duplicates_df,"\n\n")


# Task 3.
# Dropping Irrelevant Columns
# Drop the columns "Name", "Ticket", and "PassengerId" as they are not useful for prediction.

dropped_df = no_duplicates_df.drop(columns=["Name", "Ticket", "PassengerId"],inplace=False)
print("after dropping irrelevant columns",dropped_df,"\n\n")

# Task 4.
# histogram Plot
# Plot each feature frequency by histogram plot


# dropped_df.hist(bins=10, figsize=(10,8))
# plt.tight_layout()
# plt.show()

for column in dropped_df.select_dtypes(include=['int64', 'float64']).columns:
    plt.figure()
    dropped_df[column].hist(bins=10)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()