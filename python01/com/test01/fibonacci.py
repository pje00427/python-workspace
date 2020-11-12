
# 피보나치 수열
# 0 1 1 2 3 5 8 13 21 34 ...
# 앞 두개의 항을 덧셈한 결과를 매번 구해

n = int(input('양수 입력 : '))
a,b=0,1

for i in range(n):
    print(a, end=' ')
    '''
    temp=a
    a=b
    b=temp+b
    '''
    a,b=b,a+b
# 출력 0 a=1 b=0+1=1
# 출력 1 a