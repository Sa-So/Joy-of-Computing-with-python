n=int(input())
print('{',end='')
for i in range (1,n+1):
  s=i*i
  if i<n:
  	print(i,': ',s,",",sep='',end=' ')
  else:
  	print(i,': ',s,sep='',end='')
print('}',end='')
