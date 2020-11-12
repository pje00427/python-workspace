# 1. for문을 사용하여 구구단을 출력하는 함수 gugu() 함수 정의 후 메인함수에서 출력
# 2. 전달받은 단 수 만을 for문을 사용하여 구구단을 출력하는 함수 gugudan(매개변수) 함수 정의 후 메인에서 호출해보기
def gugu():
    for dan in range(2,10):
        print('<<',dan,'단>>')
        for su in range(1,10):
            print(dan, 'X', su,'=', dan*su)
        print()
def gugudan(n):
    for su in range(1,10):
        print(n,'X',su,'=',n*su)

if __name__=="__main__":
    gugudan(2)