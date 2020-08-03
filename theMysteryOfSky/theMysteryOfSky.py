 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-08-01 11:53:41
 ##

import datetime
from os import system

today = input()
date, month, year = map(int, input().split('/'))

today = today.lower()

isValidDate = True
confirm = False
weekDays= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

for day in weekDays:
    if(day == today):
        confirm = True
        break

try :
    datetime.datetime(year,month,date)
    
except ValueError :
    print ("Invalid Date")
    exit()

if(isValidDate and confirm) :

    firstDate = datetime.date(year, 1, 1)
    lastDate = datetime.date(year, month,date)
    daysCount = lastDate - firstDate
    totalDays = daysCount.days + 1
    countOfStars = totalDays % 50

    totalWeeks = totalDays // 7
    extraDays = totalDays % 7

    if (extraDays == 6):
        extraDays = 5
        
    days = (totalWeeks * 5) + extraDays
    discharge = days % 4

    if (discharge != 0):
        print(countOfStars + 1)
        system('Pause')
        
    else:
        print('Camera is Discharged')
        system('Pause')
else :
    print ("Invalid Day")
    system('Pause')