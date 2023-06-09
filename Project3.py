# Prologue: 
# Name : Numa Noorin
# 
# Description: This program loops pattern A and pattern B in ascending and descending order to display the asked image using the (+) symbol. 

# Date: 6/24/2022


# number of rows in the pattern. 
# -> Loop #1 of the pattern
print('This is Pattern A')
num_rows = 10

k = 0
for i in range(1, num_rows + 1): 
    for j in range (1, (num_rows - i) + 1): #prints symbol (+) in ascending order. 
        print(end = " ")          
    while k != (2 * i - 1):
        print("+", end = "") #this prints the symbol used in pattern. 
        k = k + 1
    k = 0   
    print()  
 
# -> Loop #2 of the pattern
print('This is Pattern B')

k = 2
m = 1
for i in range(1, num_rows): 
    for j in range (1, k):
        print(end = " ") 
    k = k + 1	  
    while m <= (2 * (num_rows - i) - 1): #prints symbol (+) in descending order. 
        print("+", end = "") 
        m = m + 1
    m = 1	
    print()
   
