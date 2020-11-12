# 반복문 - for
for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):
    print(i)
print('--------')
sum = 0
for i in range(1, 11):
    print(i, end='\t')
    sum += i

print('\n총합계: ',sum)

for i in range(10, 0, -1):
    print(i, end=' ')

print()
'''
num = int(input('양수 입력 : '))

if num>0:
    for i in range(1, num+1):
        print(i, end='')
else:
    print('양수가 아닙니다')
'''

subject = ['java','javasript','python']
for s in subject:
    print(s)
else:
    print('재밌다')

# 구구단 (2단~9단)
print('=== 구구단 ===')

for dan in range(2,10):
    print('<<', dan, '단>>')
    for su in range(1,10):
        print(dan," x ",su, '=', (dan*su))
    print()