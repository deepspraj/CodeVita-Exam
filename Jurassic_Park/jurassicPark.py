 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-06-28 13:47:21
 # @modify date 2020-06-28 20:46:06
 ##

import os

row, col = map(int,input().split(" "))

def checker (matrix,row,col,count_of_safe_places,last_row,last_col):
    if(matrix[row][col] == 'G'):
        temp1 = temp2 = temp3 = temp4 = 'W'
        if((col-1)>=0):
            temp1 = matrix[row][col-1]
        if((row-1)>=0):
            temp2 = matrix[row-1][col]
        if((row+1)<=(last_row-1)):
            temp3 = matrix[row+1][col]
        if((col+1)<=(last_col-1)):
            temp4 = matrix[row][col+1]
        if(temp1 == 'G' or temp2 == 'G' or temp3 == 'G' or temp4 == 'G'):
            count_of_safe_places.append(1)
        elif(temp1 == 'W' and temp2 == 'W' and temp3 == 'W' and temp4 == 'W'):   
            count_of_safe_places.append(1)
        else:
            count_of_safe_places.append(0)
    
    return count_of_safe_places

def get_inputs(row,col):
    matrix = []
    count_of_safe_places = []
    gates_cages = input().split(" ")
    gates_cages = list(map(int,gates_cages))

    for i in range (0,row):
        arr = input().split(" ")
        lst = [x.upper() for x in arr]
        matrix.append(lst)
    
    total_grasslands = sum([i.count('G') for i in matrix])
    matrix[gates_cages[6]-1][gates_cages[7]-1] = 'C'
    
    for i in range (0,row):
        for j in range (0,col):
            checker(matrix,i,j,count_of_safe_places,row,col)
      
    count = count_of_safe_places.count(1)
    si = (float(count)/float(total_grasslands))*100
    print(round(si, 2))
    
if((3<=row<=1000) and (3<=col<=1000)):
    get_inputs(row,col)
else:
    exit()