# try:
#     num=int(input("inter num:"))
#     num%2==0
#     print("theis is even")  
# except ZeroDivisionError as ex:
#     print(ex)




# num = int(input())
# result = 0

# while num >0:
#     rem = num%10
#     result = result+rem
#     num= int(num/10)
# print(result)

# #same
# n = int(input())
# a = n // 100
# b = n // 10 % 10
# c = n % 10
# print(a + b + c)

from math import floor
float_num = 7456.4597
float_decimal = float_num - floor(float_num)