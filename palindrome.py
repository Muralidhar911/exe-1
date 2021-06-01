a=0
big=0
small=0
d=[]
for i in range(100,1000):
	for j in range(100,1000):
		a=i*j
		


		b=str(a)
		if str(a)==(b[::-1]):
			d.append(a)
			# print(a)
			
			# if big<a:
			# 	big=a
			# 	# print(a,i,j)
			# else:
			# 	pass
print(max(d))





			

