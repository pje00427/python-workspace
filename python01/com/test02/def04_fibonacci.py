'''
# 기존에 했던 피보나치 수열
# 사용자가 숫자 입력시, 해당 입력값보다 작은 수 까지 피보나치 수열을 출력

n = int(input('정수 입력 : '))
a, b=0, 1
for i in range(n):
    print(a, end=' ')
    a, b=b, a+b
'''

# 함수로 정의해보자 ! => 사용자가 입력하는거 대신 전달값으로 숫자를 전달받고 피보나치 수열을 출력
'''
def fibonacci1(n):
    a,b=0,1
    for i in range(n):
        print(a, end=' ')
        a,b=b,a+b

if __name__=="__main__":
    fibonacci1(10)
'''
'''
#피보나치 수열을 리스트에 저장한 후 출력
result = list() # []
n = int(input('정수 입력 : '))
a,b=0,1
for i in range(n):
    # print(a, end=' ')
    result.append(a)
    a,b=b,a+b

print(result)

'''

# 함수로 정의해보자 ! => 차곡차곡 담긴 리스트를 반환하는 함수
def fibonacci2(n):
    result = list() #[]
    a,b=0,1
    for i in range(n):
        result.append(a)
        a,b=b,a+b
    return result

if __name__ == "__main__":
    print(fibonacci2(20))
