import random
# import math
from math import pi # 모듈 중에 일부만 import

def circle(x):
    return x * x * pi


if __name__ == "__main__":
    print(random.random()) #(int)(Math.random() * 10 +1)
    print(random.randint(1, 10))
    # print(math.pi)
    print(pi)
    print('원의 넓이 : ', circle(int(input('반지름 : '))))
