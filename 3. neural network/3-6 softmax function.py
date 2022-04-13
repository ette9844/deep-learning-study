# 회귀 문제 (regression)에서는 출력층에서 항등 함수를 사용한다.
# 분류 문제 (classification)에서는 출력층에서 소프트맥스 함수를 사용한다.

import numpy as np

# softmax function
def softmax(a):
  exp_a = np.exp(a)
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a
  return y

# 소프트맥스 함수 구현시에는 오버플로를 조심해야함
# 지수연산과 지수연산의 나눗셈은 입력값이 클 경우 결과가 불안정해짐
# 이를 위해 소프트맥스의 지수 함수 계산시 어떤 정수를 더하거나 빼도 결과는 동일해지는 것을 이용
# 보통 입력 신호의 최대값을 뺀다
a = np.array([1010, 1000, 990])
np.exp(a) / np.sum(np.exp(a))        # [nan, nan, nan]

c = np.max(a)                        #  입력 신호의 최대값
a - c                                # [0, -10, -20]
np.exp(a-c) / np.sum(np.exp(a-c))    # [9.99954600e-01, 4.53978686e-05, 2.06106005e-09]

# 개선된 softmax function
def softmax2(a):
  c = np.max(a)
  exp_a = np.exp(a - c)
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a
  return y

# 소프트맥스 함수의 출력은 0 에서 1.0 사이의 실수 배열이다.
# 배열의 총합은 1이 된다 (확률)

# 신경망 분류에서는 일반적으로 가장 큰 출력을 내는 뉴런만 클래스로 인식
# exp 함수는 단조 증가 함수 이기 때문에 가장 큰 출력을 내는 뉴런 위치는 변하지 않음
# 이 때문에 현업에서는 추론 단계의 출력층 소프트맥스 함수는 생략하는 것이 일반적