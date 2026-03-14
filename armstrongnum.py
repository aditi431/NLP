num = int(input("Enter number : "))
a = num
power = 0 
while(a>0):
    power += 1
    a//=10


sum = 0
k = num 

for i in range(power):
    x = num%10
    sum = sum + x**power
    num = num//10

if sum==k:
    print("Armstrong")

else:
    print("Not armstrong")




     

    

    
     