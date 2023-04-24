from visual import *
def Curve():
    curve(pos = [(-2,-2,0),(-2,0,1),(0,0,0),(3,0,0),(2,1,0),(3,4,2)],radius=0.05)
    
def Sphere():
    sphere(pos = (0,0,0),radius = 0.6,color = color.cyan,opacity = 0.75,mterial = materials.rough)
    
    
def Cone():
    cone(pos = (0,-2,0),axis = (0,4,0),radius = 2)
    
def Arrow():
    arrow(pos = (-3,0,0),axis = (5,2,0),shaftwidth = 0.5,color = color.yellow,up = (0,10,20))

def Ring():
    ring(axis = (0.5,0,0.9),radius = 0.5,thickness = 0.15)


def Cylinder():
    cylinder(pos = (-2,2,1),axis = (5,0,5),radius = 2)

def menu():
    print("---------MENU--------\n")
    print("1.Curve\n")
    print("2.Sphere\n")
    print("3.Cone\n")
    print("4.Arrow\n")
    print("5.Ring\n")
    print("6.Cylinder\n")
    print("7.Exit\n")
    
    
    while(True):
          choice = int(input("Enter your choice- "))
          if choice==1:
              Curve()
          elif choice==2:
               Sphere()
               
          elif choice==3:
               Cone()
               
          elif choice==4:
               Arrow()
               
          elif choice==5:
               Ring()
          elif choice==6:
               Cylinder()     
          elif choice==7:
               print("Exited!!")
               break
                
          else:
               print("\nINVALID CHOICE!!!")

def main():
    menu()

main()    
    

        
       
          
