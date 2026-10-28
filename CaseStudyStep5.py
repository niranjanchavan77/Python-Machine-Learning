import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

Border = "=*"*30

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

##########################################################
# Step 3 : Decide Independent and Dependent variables
##########################################################

print(Border)
print("Step 3 : Decide Independent and Dependent variables")
print(Border)

# X : Independent variable / features
# Y : Dependent variable / label

features_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"]

X = df[features_cols]
Y = df["species"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

##########################################################
# Step 4 : Visulaization of dataset
##########################################################

print(Border)
print("Step 4 : Visulaization of dataset")
print(Border)

# scatter plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label = sp)

plt.title("marvellous Iris case study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()

##########################################################
# Step 5 : Split the dataset for training and testing
##########################################################

print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border)

X_train, X_test , Y_train, Y_test = train_test_split(X,Y,test_size=0.5, random_state=42)

print("dataset spliting activity done")

print("X : ",X.shape)   # (150,4)
print("Y : ",Y.shape)   # (150,)

print("X_train : ",X_train.shape) #(75,4)
print("X_test : ",X_test.shape)   #(75,4)

print("Y_train : ",Y_train.shape)   #(75,)
print("Y_test : ",Y_test.shape)     #(75,)
