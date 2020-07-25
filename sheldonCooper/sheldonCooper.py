 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-19 16:50:51
 # @modify date 2020-07-19 17:02:24
 ##

import itertools as itt

def combinationFinder(sizeOfBottles,aConsume):
    combinations = []
    pCombinations = 0
    sizeOfBottles.sort()

    for i in range (len(sizeOfBottles)):
        if(sizeOfBottles[i] > aConsume):
            sizeOfBottles.pop(i)

    for i in itt.combinations(sizeOfBottles, 3):
        combinations.append(list(i))

    for i in range (len(combinations)):
        temp = combinations[i][0] + combinations[i][1] + combinations[i][2]
        if (temp == aConsume):
            pCombinations += 1

    print('True') if (pCombinations > 0) else print('False')

n = int(input())
sizeOfBottles = []

for i in range (n):
    sizeOfBottles.append(int(input()))

aConsume = int(input())

combinationFinder(sizeOfBottles,aConsume)