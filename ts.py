from math import *
import math
a=100000
b=0

for i in range(1,a+1):
  b=b+i
  count=0
  # print(b)
  for j in range(1,int(math.ceil(math.sqrt(b)))):
    if(b%j==0):
      count+=2
    # print(count,b)
    # if(count>=500):
    #   print(b)
  else:
    if(count>=500):
      print(b)
      break

