

import matplotlib.pyplot as plt

def graph(p,h):
    plt.plot(p,h,'ro--')
    plt.xlabel('p')
    plt.ylabel('h')
    plt.title('Pulse rate(p) vs Height(h)')
    plt.grid()
    plt.show()


def main():
    p = eval(input('Enter pulse rate in list form-  '))
    h = eval(input('Enter height in list form-  '))
    graph(p,h)

main()
