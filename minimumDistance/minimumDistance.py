 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-19 13:25:00
 # @modify date 2020-07-19 13:44:23
 ##

import math as ms

distanceA = int(input())
distanceB = int(input())
vA = int(input())
vB = int(input())

if((distanceA < 0) or (distanceB < 0) or (vA < 0) or (vB < 0)):
  print('Invalid Input')
else:
    minDistance = ms.sqrt( (distanceA * distanceA) + (distanceB * distanceB) )
    while((distanceA >= 0) or (distanceB >= 0)):
        distanceA -= vA
        distanceB -= vB
        currDistance = ms.sqrt( (distanceA * distanceA) + (distanceB * distanceB) )
        if( currDistance < minDistance ):
            minDistance = currDistance
    if(minDistance == 0.0):
        print('0.0')
    else:
        print(f'{minDistance}')