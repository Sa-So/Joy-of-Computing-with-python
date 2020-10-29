num = int(input())
check = num
flag = 0
while(check %2  == 0):
  check=check/2
  if check == 2 or check == 2.0:
    flag =100
    break
if flag == 100:
  print("YES",end = "")
else:
  print("NO",end = "")
