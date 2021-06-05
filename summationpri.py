a=[]
for num in range(2,2000000):	
	for i in range(2,num):
		if (num%i==0):
			break
	else:
		a.append(num)
		print(num)
print(sum(a))
