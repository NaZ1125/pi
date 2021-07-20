#난수를 이용한 pi값 구하기

import random

n=1000
count=0
for i in range(n):
  x=random.random()
  y=random.random()
  if(x*x+y*y<1):
    count=count+1
a=4*count/n
print(a)

#소수 2번째부터는 pi값과 일치하지 않음.