import numpy as np

# numpy 배열선언
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

# numpy 배열 산술연산 element-wise
x + y # 원소별 덧셈
x - y # 원소별 뺄셈
x * y # 원소별 곱셈
x / y # 원소별 나눗셈
# 원소 수가 다를 경우 오류 발생

# numpy 스칼라 연산 broadcast
x / 2.0

# numpy 2차원 배열 (행렬)
a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([5.0, 6.0])

a * b # 해당 연산시 b 배열이 자동으로 행렬로 broadcast 되어 계산된다

# 2차원 배열 평탄화
a = a.flatten()

# 특정 인덱스만 뽑아내기
a[np.array([0, 2, 3])]

# 특정 조건을 만족하는 원소만 뽑아내기
a[a>2]