'''
def mysum(x, y):
    return 2 * x + y

if __name__=="__main__":
    #result = mysum(2, 3)
    #print(result)
    print(mysum(2, 3))
'''
    # lamda 매개변수:리턴값
mysum = lambda x,y : 2*x+y
print(mysum(2,3))

sum = lambda a,b : a+b
print(sum(10,20))

mul = lambda a,b : a+b
print(mul(4, 5))

# 전달받은 두개의 정수값을 가지고 최소값을 반환하는
min = lambda x,y : x if x<y else y
print(min(33, 44))

max = (lambda x,y : x if x>y else y)(11, 22)
print(max)

a = lambda x : (lambda y : x+y)
b = a(100) # lambda y : 100+y
c = b(90)
print(c)
print(a(100)(90))
