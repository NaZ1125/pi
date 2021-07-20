#구분구적법을 이용한 pi값 구하기

n=1000000
s=0
for k in range(n):
  s = s + (1/n) * ( (1-(k/n)**2)**.5 ) 
print(s*4)