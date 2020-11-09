# 문자열 (single quotation과 double quotation 차이없음)

# single*1
# python's Hello World
a='python\'s Hello, World!'
print(a)
print(type(a))

# single*3
b='''python's 
Hello,  '''
# 한개랑 세개의 차이점 (3개짜리 같은 경우 안에 개행이나 따옴표 자유롭게 작성가능)
print(b)

# double*1
c="abc"
print(c)

# double*3
d="""
abc
def     "ghi" ' e' """
print(d)

#혼합
e='abc"def"ghi\npython\'s string'
print(e)

f="abc'def'ghi\nc:\ttest"
print(f)

# raw string : 역슬래시를 그냥 문자로 인식 
g=r"abc'def'\nc:\ttest"
print(g)