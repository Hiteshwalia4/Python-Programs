def csum():
	list=[]
	n = int(input("Enter number of elements- "))
	for i in range(0,n):
		e= int(input())

		list.append(e)
	print("List- ",list)

	length = len(list)
	rlist = [sum(list[0:x:1]) for x in range(0, length+1)]
	print(rlist[1:])

csum()
