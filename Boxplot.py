import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    df = pd.read_csv("iris.csv")

    sns.boxplot(x= "species", y= "petal length (cm)",data=df )

    plt.grid(True)

    plt.title("Marvellous boxplot for petal length by variety of iris")
    plt.show()

if __name__=="__main__":
    main()