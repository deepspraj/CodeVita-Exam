##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-13 21:47:01
 # @modify date 2020-07-13 22:12:36
##
 
import os

def timeCal(lst):
    ans = 0
    while True:
        if(lst[1]<lst[3]):
            instantTime = ((lst[0]+lst[1])*lst[2])
            ans = ans + instantTime 
            lst[3]=lst[3]-(lst[1]-lst[0])
        else:
            instantTime = (lst[3]*lst[2])
            ans = ans + instantTime 
            break
    return (ans) 

testCases = int(input())

if(0< testCases <=100):
    data = [[0 for x in range (4)] for n in range (testCases)]
    ans = [0]*testCases

    for i in range (testCases):
        instantData = input().split(' ')
        instantData = list(map(int, instantData))
        if(instantData[0] < instantData[1]):
            if((0 < instantData[0]) and (0 < instantData[1]) and (0 < instantData[2]) and (0 < instantData[3])):
                data[i] = instantData
        
    for i in range (testCases):
        ans[i] = timeCal(data[i])

    for i in range (testCases):
        print(ans[i])
    os.system('Pause')