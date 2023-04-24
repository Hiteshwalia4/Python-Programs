def check_num(L):
    c = 0
    for i in L:
       if i.isdigit():
           c = c + 1

    if c == len(L):
        print('All elements are numbers')
    else:
        print('All elements are not numbers')


def print_odd(L):
    c = 0
    for i in L:

            if(i % 2 != 0):
                c = c + 1
    return c        

            
        
def max_string(L):
    m = - 1
    for i in L:
        if len(i) > m:
            loc = i
            m = len(i);
    print('Maximum Sting:',loc,'Size:',m)

def reverse(L):
    l1 = L[::-1]
    print('List in reverse order:',l1)

def search(el,L):
    if el in L:
        print('Found')
    else:
        print('Not Found')

def common(L1,L2):
    l = []
    L = []
    for i in L1:
        if i not in l:
            l.append(i)

    for j in L2:
        if j not in L:
            L.append(j)

    for i in l:
        for j in L:
            if i == j:
                print('Matched element:',i)
            
L = []                          
while True:
    
         print('1. Enter the list')
         print('2. Find Every element in a list is a number')
         print('3. Count Number of odd values')
         print('4. The Largest String in a list')
         print('5. The list in reverse order')
         print('6. Find the specified element')
         print('7. Find Common Elements in two list')
         print('8. Exit')
         c = int(input("Enter the value: "))
         if c == 1:
             n = int(input('Enter the elements: '))
             for i in range(n):
                     i_v = input('Enter the element: ')
                     L.append(i_v)
                     
         if c == 2:
                     check_num(L)

         elif c == 3:
             L2=[]
             n_v = int(input('Enter the elements: '))
             for i in range(n_v):
                     i_va = int(input('Enter the element: '))
                     L2.append(i_va)
                     
             print('Number of odd values:',print_odd(L2))       

         elif c == 4:
             max_string(L)

         elif c == 5:
             reverse(L)

         elif c == 6:
             value = input('Enter the value for searching')
             search(value,L)

         elif c == 7:
             L1 = []
             n_v = int(input('Enter the elements'))
             for i in range(n_v):
                     i_va = input('Enter the element:')
                     L1.append(i_va)
             common(L,L1)          
             
         elif c == 8:
             exit(0)
