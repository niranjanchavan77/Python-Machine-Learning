import pandas as pd

Border = "="*30

##########################################################
# Step 1 : Load the Dataset
##########################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DataPath = "iris.csv"

df = pd.read_csv(DataPath)

print("dataset loaded succesfully")
print("initial entries from datasets are : ")
print(df.head())

##########################################################
# Step 2 : Data Analysis (EDA)
##########################################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of data set : ",df.shape)

print("column names : ",list(df.columns))

print("Missing values per column : ")
print(df.isnull().sum())

print("class distribution (species count)")
print(df["species"].value_counts())

print("statistical report of dataset ")
print(df.describe())