# 조건문

# if
a = 1
if a==2:
    print('a는 1입니다.')

print('반갑습니다')

# if-else
a = 10
if a==1:
     print('환영합니다')
else:
    print('안녕히가세요')

# if-else if
b = 2
if b==1:
    print('b가 1입니다')
elif b==2:
    print('b가 2입니다.')
else:
    print('b는 1도아니고 2도 아닙니다')
# test = int(input('정수 입력 :')) 입력받을 때 부터 정수로 받아도 됨
test = input('정수 입력 :')

print('입력값은 : ' + test)
print(type(test)) # str로 인식된 (정수를 입력하더라도)

if int(test)<10:
    print('사용자가 입력한 값이 10보다 작습니다.')
elif test<20:
    print('사용자가 입력한 값이 10이상 20미만입니다.')
else:
    print('사용자가 입력한 값이 10보다 큽니다')