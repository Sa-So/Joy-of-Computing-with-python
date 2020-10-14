n=int(input())
A=[]
for i in range(n):
  a=int(input())
  A.append(a)
  
A.sort()

for i in A:
  print(i,end=' ')
