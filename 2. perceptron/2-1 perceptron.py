# AND 연산을 퍼셉트론으로 구현하기
def AND(x1, x2):
  w1, w2, theta = 0.5, 0.5, 0.7
  tmp = x1*w1 + x2*w2
  if tmp <= theta:
    return 0
  else:
    return 1

AND(0, 0)
AND(1, 0)
AND(0, 1)
AND(1, 1)

# 편향 도입
import numpy as np
x = np.array([0, 1]) # 입력
w = np.array([0.5, 0.5]) # 가중치
b = -0.7 # 편향

print(np.sum(w*x) + b)

# 편향을 도입한 AND 연산
def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  tmp = sum(x*w) + b
  if tmp <= 0:
    return 0
  else:
    return 1