n=int(input())
while n>9:
  t=n
  s=0
  while t>0:
    s+=int(t%10)
    t/=10
  n=s
print(n)
