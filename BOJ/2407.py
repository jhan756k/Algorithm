# 대체 왜 class 4에 있는지 모르겠는 문제 ㅋㅋ

import math, sys
input = sys.stdin.readline
n, m = map(int, input().split())

print(math.factorial(n) // ((math.factorial(n - m)) * (math.factorial(m))))
