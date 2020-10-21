import math
(n,robot_move,x,y)=(int(input()),[],0,0)

for robot in range(n):
  dir,mag=input().split()
  if dir=='UP':
    y+=int(mag)
  if dir=='DOWN':
    y-=int(mag)
  if dir=='RIGHT':
    x+=int(mag)
  if dir=='LEFT':
    x-=int(mag)
    
print(round(math.sqrt(x*x+y*y)))
