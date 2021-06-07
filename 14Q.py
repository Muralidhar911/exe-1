
c=0
big=0
for i in range(1,1000001,2):
	n=i
	count=0
	while(n>1):
		if(n%2==0):
			n=n/2
			count+=1
			
		else:
			n=3*n+1
			count+=1
			
			if big<count:
				big=count
				c=i
			
print(c,big)



