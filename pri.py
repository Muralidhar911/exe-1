num=1
i=2
c=0
for num in range(0,100):
	if num>1:
		for i in range(2,num):
		    if(num%i==0):
		    	break
		else:
			c+=1
			if c==11:
				print(num)
				break



