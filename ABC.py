n = int(input("Enter n : ")) # no. of rows
for i in range(0,n+1):
    for j in range(0,i):
        print(chr(65+j),end =" ")
    print()

    