# tuple : list와 거의 유사
# 다만 차이점으로는 값 변경 불가(불변)

# 생성자 사용
a = tuple()
print(a)
print(type(a))

b = tuple([1, 2, 3])
print(b)

# () 사용
c = (1, 2, 3, 4)
print(c)

# 값 변경 불가
# c.append(5)

# c[10] = 10
# print(c)

d = tuple(range(1, 11)) # start <= <end
print(d)

# 튜플 합치기
#tuple+tuple
print(b + d)

# tuple을 list로 바꾸기 (형변환 같은거)
e = list(d)
print(e)

e.append('a')
print(e)

# list를 tuple로 바꾸기
f = tuple(e)
print(f)

g = (1, 2, 'str')
print(g)

h, i, j = g
print(h)
print(i)
print(j)
# g의 각 인덱스에 있던 애들이 각각 h, i, j 변수에 담김 (갯수 맞아야됨)
print(type(i))
print(type(j))

# set : 집합
# 자바 컬렉션의 set과 유사 (중복 x, 순서유지 x)

# 생성자 사용
a = set()
print(a)
print(type(a))

a.add('test')
print(a)

a = set([1, '1', '2', '3', '4', '4'])

print(a)

b = set('hello')
print(b)

# {} 사용
c = {'a', 'b', 'c','hello', 1, '1',}

