class Student:
    maxavg=0
    def __init__(self):
        self.name=input("Enter name-  ")
        self.marks=[int(input("Enter marks of subject " + str(i+1) + "-  ")) for i in range(3)]
        print()
        print("Name of student is- ",self.name)
        for i in range(3):
            print("Marks of subject",i+1,"-  ",self.marks[i])
        self.avg=0
        for i in self.marks:
            self.avg+=i
        self.avg/=3
        print("Average of student is- ",self.avg)
        print()
        if Student.maxavg < self.avg:
            Student.maxavg=self.avg

    def max_avg():
        print()
        print("Maximum average of class is-  ",Student.maxavg)

    def __del__(self):
        print("Destructor called!!!")

n=int(input("Enter no. of students-  "))
list=[]
for i in range(n):
    print("ENTER INFO FOR STUDENT ",i+1,":  ")
    list.append(Student())

Student.max_avg()

for i in list:
    del i
