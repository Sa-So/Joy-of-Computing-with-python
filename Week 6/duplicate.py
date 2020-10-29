n=input().split()
l=[]
for i in n:
  if i not in l:
    l.append(i)
    print(i,end=' ')
