def com():
	str1 = str(input("Enter string 1: "))
	str2 = str(input("Enter string 2: "))
	v,j = 0,0

	for i in str1:
		if str2.find(i)>=0 and j == str1.find(i):
			v += 1
		j += 1
	print('Number of mathcing characters: ', v)

com()
