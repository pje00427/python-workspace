# 배열 : list
# == 자바 컬렉션의 List와 유사(순서유지o, 중복저장가능)

# 생성자 사용
a = list()
print(a)
print(type(a))

# a[0] = 10
# print(a)
a.append(1)
print(a)

a[0]=10
print(a)

a.append('str')
print(a[0])
print(a[1])

# [] 사용
b = [1,2,3,4,5]
print(b)
print(b[1]+b[2])

#reverse
b.reverse()
print(b)

# 배열 정렬 : sort()
b = [1, 5, 3, 4, 2]
b.sort()
print(b)

# 중첩
c = ['a', 'b', 'c','d',['e','f','g'],'h']
print(c[4][1])

#배열 합치기
#list + list
print(b+c)