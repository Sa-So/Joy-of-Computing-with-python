n = int(input())
ans = []
for get in range(n):
  python = input().split()
  ans.append(python)
for python in range(len(ans)):
  for z in range(python+1,n):
    ans[python][z] = '0'
for code in range(len(ans)):
  if code !=  n -1:
    print(*ans[code])
  else:
    print(*ans[code],end = "")
