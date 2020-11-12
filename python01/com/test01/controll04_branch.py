# 분기문 - break, continue

i = 1
while i<=10:
    if i==5:
        break
    print(i)
    i += 1
else:
    print('출력끝') # 애초에 while문 안의 조건이 false가 되기 전에 break 빠져나왔기 때문에 출력 x
print("-------")

# 1~9까지의 홀수만을 출력
for i in range(1,10):
    if i%2 == 0:
        continue
    print(i)
else:
    print('출력끝')