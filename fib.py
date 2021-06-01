a=0
b=1
c=0
d=0
# for i in range(1,100):
while(c<4000000):
	c=a+b
	a=b
	b=c
	#if(c<=4000000):
	if(c%2==0):
		d=c+d


print(d)