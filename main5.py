###라이프니츠

import math
PI = math.pi     # 파이 (상수)
LIMIT = .000001  # 오차의 한계 (백만분의일. 상수)

n = 1; s = 1; a = 4

while(1):
  s = -s
  n = n + 1
  a = a + ( s * 4 * ( 1 / (2*n-1) ) )

  error = abs( a - PI )  # 오차
  if( error < LIMIT ):   # 오차가 충분히 작으면
    print(n, PI, a, error)
    break

#1000001항까지 급수를 계산한 결과 3.14159를 얻음.