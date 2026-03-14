'''
These are the functions that produces the output one at a time (when the value is demanded )
it is fast , complexity is O(1)

'''

# Write a loop to calculate the sum of digits of a number 
# Using only loops find the common elements between two list 
# Write a loop that goes through numbers 1 to 20 skip multiples of 4 using continue stop the loop if the no is divisible by 13
# Transpose of matrix

# def even(start , stop):
#     for num in range(start , stop+1):
#         if num%2 ==0:
#             yield num # different from other functions 

# for evenNum in even(10,50):
#     print(evenNum)
    

for i in range(0,2):
    for j in range(i):
        print(i, end = " ")
        i +=1
    print()
    
    
