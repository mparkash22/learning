

# x = 11

# if x % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# x = 0
# while x < 10:
#     if x % 2 == 0:
#         print('{} Even'.format(x))
#     else:
#         print('{} Odd'.format(x))


# #     x = x + 1

# for x in range(10):
#     if x % 2 == 0:
#         print('{} Even'.format(x))
#     else:
#         print('{} Odd'.format(x))


# for i in range(100):
#     if i == 98:
#         print(i)
#         continue
#     else:
#         print(i)

#     print('After')

# a=0
# b=1
# print(a)
# print(b)
# for i in range(10):
#     c = a + b
#     print(c)
#     a=b
#     b=c

# limit = input('Enter a number ')
# limit = int(limit)

# x = 0
# y = 1
# result = 0
# print(x)
# print(y)

# while True: # infinite while loop
#     result = x + y
#     if result > limit:
#         break
#     print(result)
#     x = y
#     y = result

# limit = input('Enter a number ')
# limit = int(limit)

# for i in (2, int(limit/2)):
#     if limit % i ==0:
#         print("not a prime")
#         exit(0)
# print("it is prime")

# limit = input('Enter a number ')
# limit = int(limit)

# def prime(number):
#     for i in (2, int(number/2)):
#         if number % i ==0:
#             print("not a prime")
#             break
#     else:
#         print("it is prime")

# prime(limit)


# def fibon(limit):
#     x = 0
#     y = 1
#     result = 0
#     print(x)
#     print(y)

#     while True: # infinite while loop
#         result = x + y
#         if result > limit:
#             break
#         print(result)
#         x = y
#         y = result

# from utils import mod

# limit = input('Enter a number ')
# limit = int(limit)

# # fibon(limit)

# # def prime(number):
# #     for i in range(2, int(number/2)+1):
# #         if number % i ==0:
# #             print("{} not a prime".format(number))
# #             break
# #     else:
# #         print("{} is prime".format(number))

# # for i in range(2,limit):
# #     mod.prime(i)

# d = list(range(10))
# print(d)

# e = list(range(10,20))

# print(e)



l = 'WASHINGTON - President Donald Trump declared on Friday (Aug 23) he would further raise American tariffs on all Chinese imports hours after China announced tariffs on American goods, the second escalation within the day of a trade war between the world’s two biggest economies that has shown no sign of ending soon'
x= l.split(' ')
print(len(x))

l = """WASHINGTON - President Donald Trump declared on Friday (Aug 23) he would further raise American tariffs on all Chinese imports hours after China announced tariffs on American goods, the second escalation within the day of a trade war between the world’s two biggest economies that has shown no sign of ending soon"""
z= l.split(" ")
print(len(z))

d = {}
for i in z:
    if i  not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1

print(d)

# from collections import Counter as c

# c = d
# print(c.most_common())

import json


