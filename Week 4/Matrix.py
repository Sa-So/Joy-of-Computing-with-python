r,c=input().split()
r=int(r)
c=int(c)
p=1
for i in range(r):
  for j in range(c):
    if(j==c-1):
      print(p,end='')
    else:
      print(p,end=' ')
    p+=1
  if(i==r-1):
    print('',end='')
  else:
  	print('')
