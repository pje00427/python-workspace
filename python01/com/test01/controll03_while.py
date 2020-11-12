# 반복문 - while
i=1
while i<=10:
    print(i)
    i+=1    # python에서는 ++
else:
    print('출력끝')

print(i)

sum=0
i=1
while i<=10:
    sum += 1
    i += 1
else:
    print('총합',sum, sep=':', end="\n")
    print('i', i, sep=":")
