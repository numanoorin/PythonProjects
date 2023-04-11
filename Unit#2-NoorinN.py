 # Name : Numa Noorin
 # 
 # Description: This program calculates and outputs the amount of money that will be in the account 
 # after the specified number of years, according to the user's input. 
 

# we need the below information (variablesP: P, r, n, & t) from user to 
# each variable is set equal to an input function, which also is wrapped 
# with a float function. 
P = float(input('Enter principal amount (in $): '))
r = float(input('Enter annual interest rate (in %):'))
n = float(input('Enter number of times per year interest has compounded:'))
t = float(input('Enter number of years account will be left to earn interest:'))

r /= 100 #interest rate is entered as a percentage so we convert into decial using this command. 
A = P * ((1 + (r / n)) ** (n * t)) # "A" variable is set equal to the principle amount multiplied by 1 + (r / n), which is then powered to (n * t)

print ('After ', t, ' years, $', format(A, ',.2f'), ' will be in the account. ', sep='')
#above line of code prints the statement using the user's input. 
