

import matplotlib.pyplot as plt

def main():
    list1=eval(input("Enter the list of integers- "))
    histogram(list1)

def histogram(list1):
    plt.hist(list1)
    plt.title("HISTOGRAM")
    plt.show()

main()
