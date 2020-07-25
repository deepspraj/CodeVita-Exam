 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-24 13:47:04
 # @modify date 2020-07-24 14:26:19
 ##

import os

n = int(input())

ans = [0 for i in range(n)]

for i in range (n):
    ans[i] = list(map(int, input().split(' ')))
    
def calculator(f,b,t,fd,bd):    
    dist = 0
    ans = 0
    forward = backward = 0
    bd = (-1) * bd
    if( (f==b) and (fd>f) ):
        print("No Ditch")
    else:
        while ( True ):
            dist = dist + f
            ans = ans + f

            if( dist >= fd ):
                forward = 1
                break

            dist = dist - b
            ans = ans + b
            
            if(dist <= bd):
                backward = 1
                break

        if(forward == 1):

            if(dist == fd):
                t = t * ans

            else:
                ans = ans - (dist - fd)
                t = t * ans

            print(f'{t} F')

        if( backward == 1 ):
            
            if( dist == bd ):
                t = t * ans

            else:
                ans = ans + (dist - bd)
                t = t * ans

            print(f'{t} B')


for i in range (n):
    calculator(ans[i][0], ans[i][1], ans[i][2], ans[i][3], ans[i][4])

os.system('Pause')