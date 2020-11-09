# 한 줄 주석
'''
    여러 줄
    주석
'''
#기본적으로 줄바꿈
print("Hello")
print('python')

'''
현재 페이지 실행 ctrl + shift + f10
'''

# end 옵션 : 출력문 뒤에 붙여줄 문구 (기본값 : \n)
print('hello', end=' ')
print('python', end="! ")
print('강보람쌤짱!')

#여러개의 값 연이어서 출력
a=26
#print('I클래스의 정원은 ' + a + '명 입니다.')
print('I 클래스의 정원은', a, '명 입니다.')
# 출력하고자 하는 값들을 ,로 나열하면 연이어서 출력 가능(사이에 기본적으로 공백이 들어감)

# sep 옵션 : 연이어서 출력시 구분자 제시
print('I 클래스의 정원은', a, '명 입니다.', sep='@', end="!")
print('hahaha')

ban= 'I 클래스'
year=2020
month=12
date=9
print(ban, '수료일은', year, '년', month, '월', date, '일')

# 자바에서의 printf와 비슷한 기능
print('%s 수료일은 %d년 %d월 %d일 입니다.'%(ban, year, month, date))
print('{0} 수료일은 {1}년 {2}월 {3}일 입니다.'.format(ban, year, month, date))
