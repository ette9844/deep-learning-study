# 앞 장에서 사용되던 활성화 함수는 임계점을 기준으로 값이 바뀌는 계단 함수(step function)

# 계단 함수
def step_function(x):
  if x > 0:
    return 1
  else:
    return 0

# numpy 배열 입력을 지원하는 계단 함수
import numpy as np
def step_function2(x):
  y = x > 0    # 각 원소의 부등호 연산 결과가 bool 배열로 리턴됨
  return y.astype(int)  # numpy 배열 자료형 변환 메서드

def step_function3(x):
  return np.array(x>0, dtype=int)

# 그래프 출력
import matplotlib.pylab as plt
x = np.arange(-5.0, 5.0, 0.1)
y = step_function3(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축 범위 지정
plt.show()
