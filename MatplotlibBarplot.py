import matplotlib.pyplot as plt

def main():
    language = ["c","c++","java","python"]
    student = [30,40,35,55]

    plt.bar(
        language,                   # x value
        student,                    # y value
        width = 0.6,                # width of bar
        edgecolor = "black",        # border color of bar
        linewidth = 1,              # width of bar bordr
        alpha = 0.8,                # transparence 0.0 to 1.0
        label = "student"           # legend text
    )

    plt.title("Marvellous bar plot")
    plt.xlabel("language")
    plt.ylabel("number of students ")

    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()