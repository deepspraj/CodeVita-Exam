 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-08-03 16:33:47
 ##

from os import system as sys
from math import gcd

def lcmFinder(lst):
    lcm = lst[0]

    for i in lst[1:]:
      lcm = int(lcm*i/gcd(lcm, i))

    return int(lcm)

n = int(input())

points = {"Sally": 0, "Darrell": 0}

n = n//2

try:
    for i in range (n):
        question = list(map(str, input().split(' ')))
        questioner = question[0]
        quest = question[1]
        
        print("{0}'s question is {1} ".format(questioner,quest))
        
        quest = list(map(int, quest.split(',')))
        
        userAnswers = input().split(' ')
        answerer = userAnswers[1]
        
        
        if(i == 0):
            firstQuestioner = questioner
            firstAnswerer = answerer
        
        correctAns = lcmFinder(quest)
        
        if (userAnswers[2] == 'PASS'):
            
            print('Question is PASSed')
            print('Answer is {0}'.format(correctAns))
            print('{0} : 0 points'.format(answerer))

        else:
            userAns = int(userAnswers[2])
            
            if(userAns == correctAns):
                print('Correct Answer')
                print('{0}: 10 points'.format(answerer))
                points[answerer] = points[answerer] + 10
                
            else:
                print('Incorrect Answer')
                print('{0}: 0 points'.format(answerer))

except:
    print('Invalid Input')
    exit()


print('\nTotal Points')
print('{0} : '.format(firstQuestioner) + str(points[firstQuestioner]) + ' points')
print('{0} : '.format(firstAnswerer) + str(points[firstAnswerer]) + ' points')

if(points[firstQuestioner] == points[firstAnswerer]):
    print('Game Result : Draw\n')
    
elif(points[firstQuestioner] < points[firstAnswerer]):
    print('Game Result : Sally is winner\n')

else:
    print('Game Result : Darrell is winner\n')

sys('Pause')