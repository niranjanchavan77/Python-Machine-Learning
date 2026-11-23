import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def main():
    # independent
    X = np.array([
        [1,2],
        [2,3],
        [3,1],
        [5,6]
        ])

    # dependent
    Y = np.array(["red","red","blue","blue"])

    new_point = np.array([[3,3]])

    print("independent variables are : ")
    print(X)

    print("dependent variables are : ")
    print(Y)

    print("testing point is : ")
    print(new_point)
    

if __name__=="__main__":
    main()