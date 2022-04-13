# 다층 퍼셉트론
# 선형 영역으로 구현할 수 없는 경우에 단층 퍼셉트론을 여러개 쌓아 비선형 영역을 구현한다. 이를 다층 퍼셉트론이라 부른다.
import numpy as np

# XOR 게이트 구현
def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  tmp = sum(x*w) + b
  if tmp <= 0:
    return 0
  else:
    return 1

def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.3
  tmp = sum(x*w) + b
  if tmp <= 0:
    return 0
  else:
    return 1
  
def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = 0.7
  tmp = sum(x*w) + b
  if tmp <= 0:
    return 0
  else:
    return 1

def XOR(x1, x2):
  w1 = NAND(x1, x2)
  w2 = OR(x1, x2)
  return AND(w1, w2)

print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))