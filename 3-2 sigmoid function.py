# 신경망에서는 활성화 함수로 시그모이드 함수(sigmoid function)를 사용
# 부드러운 S자 곡선 형태

# 시그모이드 함수
import numpy as np
def sigmoid_function(x):
  return 1 / (1 + np.exp(-x))

# 그래프 출력
import matplotlib.pylab as plt
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축 범위 지정
plt.show()