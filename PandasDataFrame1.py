import pandas as pd

def main():
    Data = {
        "Name" : ["sagar","amit","puja"],
        "Age" : [27,28,25],
        "city" : ["pune","kolhapur","satara"]
    }

    print(Data)

    print(type(Data))

    print(Data["Name"])
    
if __name__ =="__main__":
    main()