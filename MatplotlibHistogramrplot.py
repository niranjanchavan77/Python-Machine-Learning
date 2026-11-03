import matplotlib.pyplot as plt

def main():
    
    marks = [35,42,45,50,55,60,62,70,72,75,80,85,90,92]

    plt.hist(
        marks,                     # continues data
        bins=5,                     # number of group
        # error edgecolors='black',         # border color
        alpha=0.8 ,                  # transperency
        rwidth=0.9,                 # relative width bar
        
    )

    plt.title("Marvellous histogram plot")
    plt.xlabel("marks")
    plt.ylabel("frequency")

    

    plt.show()

if __name__ == "__main__":
    main()