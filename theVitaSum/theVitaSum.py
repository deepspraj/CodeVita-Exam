 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-08-01 14:52:19
 ##/

from math import factorial as fact
import os

n, k = map(int, input().split(' '))

if (k <= n):

    answer = 0

    for i in range (0,k+1,2):

        tempAnswer=fact(n)/(fact(n-i)*fact(i))
        answer=answer+tempAnswer

    print(answer)
    os.system('Pause')