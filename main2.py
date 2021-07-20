#아르키메데스 방식으로 pi값 구하기

#

import math

diameter=2 # 원의 지름 2
polygon=6 # 6각형으로 시작
side=1 # 6각형의 변의 길이는 1

n=10
for i in range(n):
    polygon = polygon * 2
    side = ( 2 - ( 4 - side**2 ) **.5 ) **.5
    pi = side * polygon / diameter
    print(polygon, ":", pi, math.pi-pi)