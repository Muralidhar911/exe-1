for i in range(1,3000):
	a=0
	for j in range(1,11):
		if(i%j==0):
			a=a+1
		else:
		    break
	if(a==10):
		print(i)
		break


