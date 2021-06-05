a=2000000
b=[1  for i in range(0,a+1)]
c=[]
for i in range(2,a+1):
	if b[i]==1:
		c.append(i)
		for j in range (i,a+1,i):
			b[j]=0
print(sum(c))
