

import matplotlib.pyplot as plt
import math

def sine():
    plt.subplot(3,1,1)
    degrees = range(0,360+1)
    sine_val = [math.sin(math.radians(i)) for i in degrees]
    plt.plot(degrees,sine_val)
    plt.xlabel('Degree')
    plt.ylabel('Sine Values')
    plt.title('Sine Curve')
    plt.grid()


def cosine():
    plt.subplot(3,1,2)
    degrees = range(0,360+1)
    cos_val = [math.cos(math.radians(i)) for i in degrees]
    plt.plot(degrees,cos_val)
    plt.xlabel('Degree')
    plt.ylabel('Cosine Values')
    plt.title('Cosine Curve')
    plt.grid()

def polynomial(lis):
    plt.subplot(3,1,3)
    y1 = [(t**2)+t+1 for t in lis]
    y2 = [math.exp(t) for t in lis]
    plt.plot(lis,y1,'ro--',label='X vs X^2+X+1')
    plt.plot(lis,y2,'b<-.',label='X vs e^x')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('X vs X^2+X+1 and X vs e^x')
    plt.grid()

def main():
    lis=eval(input("Enter the list-  "))
    
    sine()
    cosine()
    polynomial(lis)
    plt.tight_layout()
    plt.show()

main()
