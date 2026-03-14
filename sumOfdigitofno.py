n = int(input("Enter n : "))
sum = 0
while n > 0 :
    d = n%10
    sum = sum + d
    n //= 10
print(sum)

