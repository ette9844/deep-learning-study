# 최근에는 시그모이드 대신 ReLU(Rectified Linear Unit - 렐루)함수를 주로 이용
# 입력이 0을 넘으면 그 입력을 그대로 출력하고 0이하면 0을 출력하는 함수

import numpy as np
def relu(x):
  return np.maximum(0, x)
# numpy maximum: 두 입력 값 중 큰 값을 선택해 반환

# 그래프 출력
import matplotlib.pylab as plt
x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1.0, 6.0) # y축 범위 지정
plt.show()