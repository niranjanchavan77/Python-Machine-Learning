import pandas as pd

def main():
    Data = {
        "Name" : ["sagar","amit","puja"],
        "Age" : [27,28,25],
        "city" : ["pune","kolhapur","satara"]
    }

    dobj = pd.DataFrame(Data)

    print(dobj[["Age","Name"]])
    
if __name__ =="__main__":
    main()