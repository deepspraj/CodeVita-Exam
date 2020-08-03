 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-29 23:51:16
 ##

import os

def winner(n):
    chances = n//4
    
    if(chances%2 == 0):
        remain = n - (chances*4)
        if(remain%2 == 0):
            print("No")
        else:
            print("Yes")
    
    else:
        remain = n - (chances*4)
        
        if(remain%2 != 0):
            print("No")
        else:
            print("Yes")

testCase = int(input())

data = []

for i in range (testCase):
    temp = int(input())
    data.append(temp)
    
for i in range (testCase):
    winner(data[i])

os.system('Pause')