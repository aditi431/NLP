# write recursive program to find fibonnaci series


def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter no. of terms"))
for i in range(0,n):
    print(fib(i),end = " ")

# incryption - scissor sypher text
# Pascals triangle
# reverse no. using recurssion
# check num is armstrong or not
