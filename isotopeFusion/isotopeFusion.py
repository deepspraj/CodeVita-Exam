 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-31 16:50:27
 ##

import os
from math import sqrt 

def isotopeFusion(dataList):

    confirm = False
    dataList.sort()
    num = sqrt(len(dataList))
    num = int(num)
    newLength = len(dataList)//num
    executableList = []

    for i in range (newLength):
        newList = []
        
        if((i%2)==0):
            for j in range (num):
                newList.append(dataList[j])
            
            for j in range (num):
                dataList.pop(0)   
                
            newList.sort()
            executableList += newList
            confirm = True
            
        else:
            for j in range (1,num+1):
                newList.append(dataList[-j])
                
            for j in range (num):
                dataList.pop(-1)     
                
            executableList += newList
            confirm = False
            
        newList.clear()

    if (len(dataList) > 0):
        if (confirm == True):
            dataList.sort(reverse = True)
            
        executableList += dataList

    temp = executableList[0]
    answer = 0
    
    for i in range (1,len(executableList)):
        tempAnswer = temp * executableList[i]
        
        answer += tempAnswer
        
        if(tempAnswer > 198):
            temp = tempAnswer%199
        else:
            temp = tempAnswer

    print(str(answer) + " KJ")

n = int(input())

if (0 < n < 1000):
    dataList = list(map(int, input().split(' ')))

    i = 0
    
    try:
        while (True):
            temp = dataList[i]
            if ((temp > 198) or (0 >= temp)):
                print('Invalid Input')
                exit()

            i += 1

            if(i == n):
                break
    except IndexError:
        print(f'Oooops!!\nIncomplete Sequence\n{n-i} atom(s) are missing')
        exit(0)
        
    if (len(dataList) > n):
        del dataList[n:len(dataList)]

isotopeFusion(dataList)

os.system('Pause')