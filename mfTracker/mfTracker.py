 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-27 19:27:10
 ##

import numpy as np
import os 

def solver(shares, amount):
    if (len(shares) == len(amount)):
        try:
            equations = np.array(shares)
            answers = np.array(amount)
            solutions = np.linalg.solve(equations,answers)
            
            for i in range (len(solutions)):
                print(round(solutions[i], 2))
        except:
            print('Unsolvable')
    else:
        print('Please check the inputs')

amount = []
shares = []

n = int(input())

for i in range (n):
    share = list(map(int,input().split(' ')))
    amountR = share[-1]
    share.pop(-1)
    shares.append(share)
    amount.append(amountR)

solver(shares, amount)
os.system('Pause')