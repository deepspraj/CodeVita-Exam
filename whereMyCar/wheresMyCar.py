 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-16 18:16:23
 # @modify date 2020-07-16 20:47:01
 ##

import math as ms
import os

row, col, parkId, cap = map(int,input().split(' '))
matrix = [[0 for i in range (col)] for j in range (row)]
dataBase = {}

def parking(x,y,carNumber,dataBase):
    locationX = locationY = 0
    for i in range(x+1):
        for j in range(y+1):
            if(matrix[i][j] == 'PL'):
                locationX = i
                locationY = j
    if(dataBase.get((locationX,locationY)) == ''):
        tempData = [carNumber]
    else:    
        tempData = [dataBase.get((locationX,locationY)), carNumber]
    dataBase[locationX,locationY] = tempData
    
def retreival(carNumber,dataBase,cap):
    for i in range (row): 
        for j in range (col):
            try:  
                currBase = dataBase.get((i,j))
                for k in range (len(currBase)):
                    if(currBase[k] == carNumber):
                        
                        print(i, j, ms.floor(k/cap),(k%cap)+1)
                        return None
            except:
                print(end='')
parkingLots = 0

for i in range (row): 
    for j in range (col):
        if (i%parkId == j%parkId == 0):
            dataBase[i,j] = ''
            matrix[i][j] = 'PL'  
            parkingLots += 1

testCase = int(input())

events = []
retreivals = []

for i in range(testCase):
    events = input().split(' ')
    if(events[0] =='P'):
        parking(int(events[1]),int(events[2]),events[3],dataBase)
    elif(events[0] == 'R'):
        retreivals.append(events[1])

print(parkingLots)
for j in range (len(retreivals)):
    retreival(retreivals[j],dataBase,cap)
os.system('Pause')