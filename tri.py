a=1
b=2
while (a>0):
	
	c=0

	for i in range(1,b+1):
		count=0
		c+=i
		
	b+=1
	print(c)
	# print(b,"b")	
	for i in range(1,c+1):
		if c%i==0:
			count+=1

	if count >=200:
		print(c)
		break

