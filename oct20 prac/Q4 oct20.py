
def asc_str():
    ans = []
    ls = list(input("Enter list of Numbers - ").split())
    ls2 = list(map(int , ls))
    print(ls2)
    for i in ls:
        for j in range(len(i)-1):
            if int(i[j])>int(i[j+1]):
                break;
        else:
            ans.append(i)
    ans = list(map(int , ans))
    print(ans)
    
asc_str()
