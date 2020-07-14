 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-13 09:57:25
 # @modify date 2020-07-13 10:43:09
 ##

import os
import math as ms

def collectingCandies(countOfBoxes,sub):
    if(len(sub)%2 == 0):
        totalTime = 0
        temp = [0 for j in range(countOfBoxes)] 
        instantTime = 0
        for i in range (countOfBoxes):
            instantTime = instantTime + sub[i]
            if(i != 0):
                temp[i-1] = instantTime
        for i in range (len(temp)):
            totalTime = totalTime + temp[i]
        return (totalTime)
    else:
        firstHalf =  ms.ceil(len(sub)/2)
        temp = [0 for j in range(countOfBoxes)]
        totalTime = instantTime = 0
        for i in range(firstHalf):
            instantTime = instantTime + sub[i]
            if(i != 0):
                temp[i-1] = instantTime 
        instantTime = 0
        for i in range(firstHalf, len(sub)):
            instantTime = instantTime + sub[i]
            if(i != firstHalf):
                temp[i] = instantTime
                
        instantTime1 = temp[firstHalf-2]
        instantTime2 = temp[-1]
        temp.sort()
        temp[0] = instantTime1 + instantTime2
        temp.sort()
        for i in range (len(sub)):
            totalTime = totalTime + temp[i]
        return totalTime

testCases = int(input())

if(0<testCases <=10):
    candiesInBoxes = [[0] for x in range(testCases)]
    answers = [[0] for x in range(testCases)]
    for currCase in range (testCases):
        noBoxes = int(input())
        if(0<noBoxes<=10000):
            lst = input().split(' ')
            lst = list(map(int, lst))
            candiesInBoxes[currCase] = lst
     
    for i in range (testCases):           
        answers[i] = collectingCandies(len(candiesInBoxes[i]),candiesInBoxes[i])
    
    for i in range (testCases):
        print(str(answers[i]) + " seconds")

    os.system('Pause')