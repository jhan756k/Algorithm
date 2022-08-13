# 파이썬에서는 asterisk 가 4가지로 사용됨

# 1. 곱셈
# 2. 수열 확장
# 3. 가변인자
# 4. 가변할당

# 가변인자

def function(a, b = None): # b는 None 이 디폴트값
    pass
# 이런 함수에서 a 는 positional argument, b 는 keyword argument 임 (a는 필수, b는 선택)

# 이때 인자에 *args 혹은 **kwargs라는 것은 가변인자;
# args 는 list/tuple, kwargs는 dict 에 저장됨

def args_function(*args):
    print(args)

def kwargs_function(**kwargs):
    print(kwargs)
    
args_function('a', 'b') # ('a', 'b')
kwargs_function(a = 100, b = 200) # {'a':100, 'b':200}


# 가변할당

# 말그대로 가변적으로 할당함
test = [1, 2, 3, 4, 5]

*a, b = test 
print(a, b) # [1, 2, 3, 4], 5

a, *b, c = test
print(a, b, c) # 1, [2, 3, 4], 5

# 위 코드를 보면 매개변수의 개수에 맞춰 할당되는 것을 알 수 있음.

# 이를 이용하면 리스트 언패킹도 가능

test = [1, 2, 3, 4]
print(*test) # 1 2 3 4 
# c++ 포인터 선언하는거 마냥 배열 혹은 튜플 앞에 * 붙이고 출력하면 for loop 의 효과를 한줄에; 
