# 산술연산
a=21
b=2
print(a+b)
print(a-b)
print(a*b)
print(a**b) # 제곱
print(a/b) # 실수형 그 자체로
print(a//b) # 몫
print(a%b) # 나머지

# 비교연산 (동등비교, 대소비교)
a, b=5, 3
print(a == b)
print(a != b)
print(a > b)
print(a <= b)
print(a is b)
print(a is not b)

# 논리 연산
print(True or False)
print(False and True)

# 논리 부정 연산
print(not False)


list01 = list(range(10, 20)) # 10 ~ 19
print(list01)

list02 = list(range(100)) # 0 ~ 99
print(list02)

print(list02[2])
# 범위 연산
print(list02[12:49]) # 12 ~ 48
print(list02[12:49:3])

# [start:end] => start ~ end-1
# [start:end:step] => start ~ end-1 까지 step만큼씩 증가

str='Hello World!'
print(str)
print(str[0])
print(str[0:5])
print(str[6:11])
print(str[0:4] * 2)

# 멤버 연산
list03 = [0, 1, 2, 3, 4, 5]
print(3 in list03)
print(5 not in list03)
print(6 not in list03)


