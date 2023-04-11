# Prologue: 
# Name : Numa Noorin
# 
# Description: This program reads the contents of the Gas Prices file from 1994 on a 
# weekly basis and then displays the graph. 



import matplotlib.pyplot as plt
import numpy as np

def main():
    print("Welcome to my program. This program will read data off a file called 1994_Weekly_Gas_Averages.txt. It will "
        "plot the data on a line graph.")
    print()

    gasFile = "1994_Weekly_Gas_Averages.txt"

    gasList = np.loadtxt(gasFile)
    y_coords = range(1, len(gasList) + 1)

    # builds line graph
    plt.plot(gasList, y_coords)

    # adds title
    plt.title('1994 Weekly Gas Averages')

    # add labels
    plt.xlabel('Gas Averages')
    plt.ylabel('Week')

    
    # displays the graph
    plt.show()


if __name__ == "__main__":
  main()
