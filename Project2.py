# Prologue: 
# Name : Numa Noorin
# 
# Description: This program gives the user options to choose Package A, B, C or D. 
# the according to user's input it calculates the user's monthly bill for selected plan. 
# User then is asked how many minutes of usage are expected from the package
# and lastly it prints the user's selected package along with monthly billing amount. 

# Date: 6/22/2022


import math

def main():  
    base_price_A = float(29.95) 
    base_price_B = float(39.95) 
    base_price_C = float(49.95) 
    base_price_D = float(69.95) 
    expected_min_A = float(500) 
    expeced_min_B = float(600)
    expeced_min_C = float(800)
    expeced_min_B = float(inf) 

print('Package A: For $29.95 per month 500 minutes are provided. Additional minutes are $0.25 per minute.')
print('Package B: For $39.95 per month 600 minutes are provided. Additional minutes are $0.35 per minute.')
print('Package C: For $49.95 per month 800 minutes are provided. Additional minutes are $0.40 per minute.')
print('Package D: For $69.95 per month unlimited minutes provided.')


package = input("Enter your package selection:")

input_options = {"A":"Package A","B":"Package B", "C":"Package C", "D":"Package D"} 

min_usage = input("How many minutes do you expect to use of the selected service?")

result = print("The selected monthly cost for your plan is ")

    