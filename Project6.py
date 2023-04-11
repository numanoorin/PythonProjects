# Prologue: 
# Name : Numa Noorin
# 
# Description: This program performs the following calculations: Average price per year and month, 
# lists the price high to low, and low to high, 


#Opening GasPrice.txt 
infile = open('C:/Users/numanoorin/Desktop/Summer2022/Python/Unit#8-NoorinN/GasPrice.txt')
 
#Read file content using deadline 
gasPrices = float(infile.readline())
 
count = 0
# Strips the newline character 
for line in gasPrices:
    count += 1
    print("Line{}: {}".format(count, line.strip())) 

#Find the average price per year 
averagePricePerYear = sum(gasPrices)/len(gasPrices)
#Find the average price per month 
averagePricePerMonth = sum(gasPrices)/12
#Find Highest price per year
print('Highest is ', max(gasPrices))
#Find Lowest price per year
print('Lowest is ', min(gasPrices))
#Find list of price, Lowest to Highest
sorted_gasPrice = sorted(gasPrices) 
print(sorted_gasPrice)
#Find list of price, Highest to Lowest
desendingOrder=gasPrices.sort(reverse = True) 
print(desendingOrder)

