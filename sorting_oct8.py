def Linear_search(L, S):
    for i in range(len(L)):
        if L[i] == S:
            Loc = i
            return Loc
    else:
        return -1

def Lin_s_rec(L, S, i):
    if (i < len(L)):
        if L[i] == S:
            Loc = i
            return Loc
    else:
        return -1
    Lin_s_rec(L, S, i + 1)


def binary_search(L, S):
    low = 0
    h = len(L) - 1
    while (low <= h):
        mid = int((low + h) / 2)
        if (L[mid] == S):
            return mid
        elif (L[mid] < S):
            low = mid + 1
        elif (L[mid] > S):
            h = mid - 1
    return -1

def binary_serch(L, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if L[mid] == x:
            return mid
        elif L[mid] > x:
            return binary_serch(L, low, mid - 1, x)
        else:
            return binary_serch(L, mid + 1, high, x)
    else:
        return -1


def bubble_sort(L):
    for i in range(len(L) - 1):
        for j in range(len(L) - i - 1):
            if (L[j] > L[j + 1]):
                temp = L[j]
                L[j] = L[j + 1]
                L[j + 1] = temp

def selection_sort(L):
    for i in range(len(L) - 1):
        mine = i
        for j in range(i + 1, len(L)):
            if (L[j] < L[mine]):
                mine = j

        temp = L[i]
        L[i] = L[mine]
        L[mine] = temp


def insertion_sort(L):
    for i in range(1, len(L)):
        k = L[i]
        j = i - 1

        while (j >= 0 and k < L[j]):
            L[j + 1] = L[j]
            j = j - 1
        L[j + 1] = k

L = ["Amit", "Rohan", "Rishi"]
print(L)
while (True):
    print("1.Linear Search(iterative)")
    print("2.Linear Search(recursive)")
    print("3.Binary Search(iterative)")
    print("4.Binary Search(recursive)")
    print("5.Bubble Sort")
    print("6.Selection Sort")
    print("7.Insertion Sort")
    print("8.Exit")
    ch = int(input("Enter the value- "))
    if ch == 1:
        Name = input("Enter the Name-  ")
        print("Index", Linear_search(L, Name))

    if ch == 2:
        Name = input("Enter the Name- ")
        print("Index", Lin_s_rec(L, Name, 0))

    if ch == 3:
        Name = input("Enter the Name-  ")
        print("Index", binary_search(L, Name))

    if ch == 4:
        Name = input("Enter the Name- ")
        print("Index", binary_serch(L, 0, len(L) - 1, Name))

    if ch == 5:
        bubble_sort(L)
        print(L)

    if ch == 6:
        selection_sort(L)
        print(L)

    if ch == 7:
        insertion_sort(L)
        print(L)

    if ch == 8:
        exit(0)