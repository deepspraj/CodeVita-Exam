 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-11 16:10:38
 # @modify date 2020-07-11 17:23:57
 ##

import os

num = int(input())
num += 1

def firstPart(n):
    k = 0
    for i in range(1, n+1):
        for space in range(1, (n-i)+1):
            print(end='  ')
        while k != (2*i-1):
            print('*', end=' ')
            k += 1
        k = 0
        print()

def secondPart(n):
    k = 0
    a = 3
    for i in range (0, n-2):
        for space in range(0, n-i-2):
            print(end='  ')
        while k != a:
            print('*', end=' ')
            k += 1
        a += 2
        k = 0
        print()

def lastPart(n):
    k = 0
    a = 3
    for i in range (0, n-3):
        for space in range(0, n-i-2):
            print(end='  ')
        while k != a:
            print('*', end=' ')
            k += 1
        a += 2
        k = 0
        print()

def stand(num):
    for i in range (0,2):
        for j in range (0,(2*num)-2):
            print(end=' ')
        print('*')
        
if(num <= 2):
    print('You cannot generate christmas tree')

elif(num > 20):
    print('Tree is no more')

else:
    firstPart(num)
    part = 1
    new = num
    for i in range (0 , num-4):
        if (part < num):
            secondPart(new)
            part += 1
    lastPart(num)
    stand(num)
    os.system('pause')