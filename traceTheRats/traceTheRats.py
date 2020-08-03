 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-30 00:57:48
 ##

#import os

def confirmation(x,y):
    temp1 = temp2 = temp3 = temp4 ="X"
    count = 0

    if(matrix[x][y] == 'O'):
        try:
            temp1 = matrix[x][y-1]
        except:
            print(end='')
        try:
            temp2 = matrix[x][y+1]
        except:
            print(end='')
        try:
            temp3 = matrix[x-1][y]
        except:
            print(end='')
        try:
            temp4 = matrix[x+1][y]
        except:
            print(end='')
            
    if((temp1 == 'O') or (temp2 == 'O') or (temp3 == 'O') or (temp4 == 'O')):
        count += 1
    
    if(count == 1):
        print("Yes")
    else:
        print("No") 

n = int(input())

matrix = []

for i in range (n):
    temp = list(input().split(' '))
    
    if(len(temp) == n):
        for i in range (n):
            temp[i] = temp[i].upper()
    else:
        print('The input are not according to conditions ')
        exit()    
    if(len(temp) == n):
        matrix.append(temp)

noOfRats = int(input())
location = []

for rat in range (noOfRats):
    x, y = map(int, input().split(' '))
    if( x and y <= n ):
        location.append([x,y])
        
for i in range (len(location)):
    confirmation(location[i][0]-1,location[i][1]-1)
    


#os.system('Pause')