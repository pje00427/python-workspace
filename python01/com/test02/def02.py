
def func01(x, y):
    print('파라미터로', x, '와', y, '두 개가 들어왔습니다')
    # x + y = xx
    print('{0} + {1} = {2}'.format(x, y, x+y))

def func02(x, y):
    print('매개변수 있고 반환값 있는 함수')
    return x+y

def func03(x, y):
    print('매개변수 있고 반환값이 두개인 함수')
    return x+y,x-y
if __name__=="__main__":
    # func01(5,6)
    # print(func02(1,3))
    # result = func03(4,7)
    # print(result)
    sum, minus = func03(4,7)
    print(sum)
    print(minus)