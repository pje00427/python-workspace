def func01():
    print('매개변수 없고 반환값도 없는 함수')

def func02():
    return '매개변수 없고 반환값은 있는 함수'

def func03():
    print('매개변수 없고 배열을 반환하는 함수')
    return ['java', 'python']

def func04():
    print('매개변수 없고 dictionary를 반환하는 함수')
    return{1:'a',2:'b'}

def func05():
    print('매개변수 없고 여러개의  결과값을 반환하는 함수')
    return 1,2

# 프로그램의 주 진입점
if __name__ == "__main__":
    print('프로그램 시작시 가장 먼저 호출됨 (자바에서의 main메소드 같은 느낌)')
    # func01()
    # print(func02())
    # arr = func03()
    # print(arr)
    # print(type(arr))
    # print(func03()[1])

    # print(func04()[2])
    result = func05() # 반환값이 여러개일 경우 tuple로 반환
    print(type(result))
    print(result[1])