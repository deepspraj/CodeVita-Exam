 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-20 20:56:40
 # @modify date 2020-07-20 21:49:23
 ##

import math

def scheduler(n,sequence):
    
    limit = int(n/2)
    schedule = []
    firstHalf = []
    secondHalf =[]

    for i in range (limit):
        firstHalf.append(i+1)
        
    for i in range(n,limit,-1):
        secondHalf.append(i)

    for i in range (n-1):
        for j in range (limit):
            temp = [firstHalf[j],secondHalf[j]]
            schedule.append(temp)
        
        
        temp1 = firstHalf[-1]
        temp2 = secondHalf[0]
        firstHalf.insert(1,temp2)
        firstHalf.pop(-1)
        secondHalf.pop(0)
        secondHalf.append(temp1)

    schedule = 2 * schedule

    noOfDays = math.ceil(len(schedule) * 2 / 3)

    j = 0

    while (i < noOfDays):
        
        if (i%2 == 0):
            team1 = "T" + str(schedule[j][0]) + " vs " + "T" + str(schedule[j][1])
            j += 1
            team2 = "T" + str(schedule[j][0]) + " vs " + "T" + str(schedule[j][1])
            j += 1
            print(team1, end='     ')
            print(team2)
        
        else:
            team1 = "T" + str(schedule[j][0]) + " vs " + "T" + str(schedule[j][1])
            j += 1
            print(team1)
        
        print()
        
        i += 1

n = int(input())

if( (8 <= n <= 100) and (n%2 == 0)):
    sequence = map(int,input().split(' '))
    scheduler(n,sequence)
else:
    print('Input is not according to the conditions')