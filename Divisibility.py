a=int(input())
l=[]
for i in range(1,51):
  l.append(i)

count=0

for i in l[a:]:
  if(i%a==0):
    count+=1

print(count)


    
#OR
#if(a<51):
#  d=int(50/a)
#  print(d-1)
#else:
#  print(0)
