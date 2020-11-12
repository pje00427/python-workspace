'''
*
**
***
****
*****
print('*' * 1)
print('*' * 2)
print('*' * 3)
print('*' * 4)
print('*' * 5)
'''
for i in range(5):
    print('*' * (i+1))

for i in range(5):
    print('*' * (5-i))
'''
*****
****
***
**
*
'''

'''
    *
   **
  ***
 ****
***** 
'''
for i in range(5):
    print (' ' * (4-i) + '*' * (i+1))

'''
*****
 ****
  ***
   **
    *
'''
for i in range(5):
    print(' ' * i + '*' * (5-i))