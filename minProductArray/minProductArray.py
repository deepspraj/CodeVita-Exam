 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-10 16:07:01
 # @modify date 2020-07-10 16:07:01
 ##

import os

n ,k = map(int, input().split(' '))

def minSumCal(n, k):
    listOne = input().split(' ')
    listOne = list(map(int,listOne))
    listTwo = input().split(' ')
    listTwo = list(map(int,listTwo))
    maxDiff = 0
    minSum = 0

    for i in range (0, n):

        product = listOne[i] * listTwo[i]
        
        if ( product < 0 and listTwo[i] < 0):
            temp = (listOne[i] +  2  * k ) * listTwo[i]
        elif( product < 0 and listOne[i] < 0):
            temp = (listOne[i] - 2 * k) * listTwo[i]
        elif( product > 0 and listOne[i] < 0):
            temp = (listOne[i] + 2 * k) * listTwo[i]
        elif (product > 0 and listOne[i] > 0):
            temp = (listOne[i] - 2 * k)  * listTwo[i]
        
        diff =  abs(product - temp)

        if( diff > maxDiff ):
            maxDiff = diff
            
        minSum = minSum + product
        
    minSum = minSum - maxDiff

    print(minSum)

if ((1 <= n <= 100000) and (0 <= k <= 1000000000)):
    minSumCal(n,k)
    os.system('Pause')
