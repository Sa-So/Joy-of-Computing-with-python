a, b = input().split()
a=int(a)
b=int(b)
l=[]
for i in range(1,51):
  l.append(i)
  
for i in l[a:b]:
  print(i)

#OR
#for i in range(a+1,b+1):
#  print(i)
