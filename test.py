# a = [1,2,3,4,5]
# b = []
# for i in range(len(a)-2):
#     sum_number = a[i]+a[i+1]+a[i+2]
#     b.append(sum_number)
# print(b)

# add = lambda x,y:x+y
# print(add(2,3))

'''
Lambda functioms are used when u need a small , one line function that does not need to be renamed unlike regular functions lambda functions are limited
to a single line expression this make them concise but restrictive.

'''
square = lambda x:x**2

print(square(3))

# Higher order functions:
'''
These are the functions that take other functions or return other functions '''