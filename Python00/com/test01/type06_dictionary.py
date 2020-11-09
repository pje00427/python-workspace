# dictionary(dict)
# 자바 컬렉션의 Map과 유사(key-value 세트로 (key중복x), 순서유지x)

a = dict()
print(a)
print(type(a))

a[1] = 1
a[2] = 2
print(a)

a['test'] = 'a'
print(a)

# {} 사용
b={}
print(b)

b={'one':1, 'two':2}
print(b)
b['one'] ='this is one'
print(b)

# list : []  List (가변)
# tuple: ()  List (불변)
# set  : {}  Set  index 개념없음
# dict : {}  Map  index 대신 key값으로 