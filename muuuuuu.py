a=102
r=int(a)
k=1
count=0
for i in range(1,r+1):
  b=bin(i).replace("0b","")
  c=0
  for j in range(len(b)-2):
    if(b[j]+b[j+1]+b[j+2]=="101"):
      c=c+1
  if(c>=k):
    count=count+1
print(count)