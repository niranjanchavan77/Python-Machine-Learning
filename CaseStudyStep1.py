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