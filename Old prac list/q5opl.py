def sales():
	week1 = int(input("Enter sales done in week 1: "))
	week2 = int(input("Enter sales done in week 2: "))
	week3 = int(input("Enter sales done in week 3: "))
	week4 = int(input("Enter sales done in week 4: "))
	monthlySales = week1 + week2 + week3 + week4
	commision = 0
	remark = ""
	if(monthlySales>50000):
		commision = 0.5
		if(monthlySales>=80000):
			remark = "Excellent"
		elif(monthlySales>=60000 and monthlySales< 80000):
			remark = "Good"
		elif(monthlySales>=40000 and monthlySales<60000):
			remark = "Average"
	else:
		remark = "Work Hard"

	print("Total Sales: ", monthlySales)
	comissionAmount = commision * monthlySales
	print("comission Amount: ", comissionAmount)
	print(remark)

sales()
