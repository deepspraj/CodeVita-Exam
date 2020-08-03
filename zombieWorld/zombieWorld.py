 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-30 15:24:28
 ##

import os

def zombieWorld(n, t, e, p, d):
    
    for i in range (len(e)):
        if (e[i] <= p):
            temp = (p - e[i])
            p += temp
           
    if((p >= d)):
        print('Yes')
    else:
        print('No')
    
testCase = int(input())

energyOfZombies = []
zombies = []
time = []
playerEnergy = []
advanceLevel = []

if(0 < testCase <= 10):
    for test in range (testCase):
        instantZombies, instantTime = map(int, input().split(' '))
        
        if((0 < instantZombies <= 50) and (0 < instantTime <= 100)):
            zombies.append(instantZombies)
            time.append(instantTime)
            
            energies = list(map(int, input().split(' ')))
            
            if (len(energies) == instantZombies):
                energyOfZombies.append(energies)
            
            instantPlayerEnergy, minimumEnergy = map(int, input().split(' '))
            
            if ((0 < instantPlayerEnergy <= 2000) and (0 < minimumEnergy <= 500)):
                playerEnergy.append(instantPlayerEnergy)
                advanceLevel.append(minimumEnergy)
    
if (len(energyOfZombies) == testCase):
    for i in range (testCase):    
        try:
            zombieWorld(zombies[i],time[i],energyOfZombies[i],playerEnergy[i],advanceLevel[i])
        except IndexError:
            print('Test Case ' + str(i+1) + ' failed due inappropriate input')
    os.system('Pause')
else:
    print('Provided Inputs are not according to the conditions')