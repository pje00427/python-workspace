#split

str1 = 'hello, world\nHello,python'
print(str1)

arr1 = str1.split(' ')
print(arr1)

print(type(arr1))

#join
arr2 = ['1', '2', '3', '4']
print(arr2)

str2 = '+'.join(arr2)
print(str2)
print(type(str2))
print(eval(str2))
