# # for i in range (0,5):
# #     print(" ","*"," ")
# #     i +=1
# # for j in range(0,5):
# #     print(" ","**"," ")
# #     j += 1



# print(" " , "*"," ")
# print("*"," "," ")
# print("***"," ")
# print(" ","****"," ")
# print(" ","*****"," ")

r = int(input("Enter r : "))
for i in range(0,r+1):
    print(" "*(r-i),end = " ")
    for j in range(0,i):
        print("*",end = " ")
    print()

n = int(input("Enter n : ")) # no. of rows
for i in range(0,n+1):
    for j in range(0,i+1):
        print(chr(65+j),end =" ")
    