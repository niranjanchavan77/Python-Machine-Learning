import pandas as pd

def main():
    sobj = pd.Series([11,21,51,101],index = ["c","c++","java","python"])

    print(sobj)

    print(sobj["python"])
    
if __name__ =="__main__":
    main()