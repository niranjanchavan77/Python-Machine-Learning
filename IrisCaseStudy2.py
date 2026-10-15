from sklearn.datasets import load_iris

def main():
    print("="*30)
    print("iris classification case sutdy")
    print("="*30)

    Dataset = load_iris()

    # meta data of the Dataset

    print("Indipendent variables are : ")
    print(Dataset.feature_names)

    print("Deoendent variables are : ")
    print(Dataset.target_names)

if __name__ =="__main__":
    main()