for i in range(1,3000):
	# print(i)
	count=0
	for j in range(1,11):
		if i%j==0:
			count+=1
			# print(count)
		else:
			break
	
	if j==10:
		print(i)
		break

			
			
		
