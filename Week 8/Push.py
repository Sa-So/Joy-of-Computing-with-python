n=input().split()
c=0
for i in range(len(n)):
  if n[i]!='0':
    print(n[i],end=' ')
  else:
  	c+=1
for i in range(c):
  print('0 ',end='')
