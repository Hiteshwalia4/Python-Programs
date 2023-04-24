def get_value(data_list,index):
    try:
        return data_list[index]
    except IndexError:
        return None

n=int(input("Enter no. of elements in list-  "))
el=input("Enter the element- ")
list=[el for i in range(n)]
index_number=int(input("Enter index no.- "))
value=get_value(list,index_number)
print(value ," is present at index",index_number)        
