import matplotlib.pyplot as plt

def main():
    Study_hour = [1,2,3,4,5,6]
    marks = [35,42,50,62,72,85]

    plt.scatter(
        Study_hour,
        marks,
        s = 100,
        marker = "*",
        alpha=0.8,
        edgecolors="black",
        linewidths=1,
        label = "student"
    )

    plt.title("Marvellous scatter plot")
    plt.xlabel("study hour")
    plt.ylabel("marks of students ")

    plt.grid(True)
    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()