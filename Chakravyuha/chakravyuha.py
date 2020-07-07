 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-07 16:15:06
 # @modify date 2020-07-07 16:15:06
 ##



import os

n = int(input())

def chakravyuha(n):
    points = 0
    points_location = []
    b = d = n
    matrix = [[0 for j in range(b)] for i in range(b)]
    num = 1
    
        # a - starting index of row  
        # b - ending index of row  
        # c - starting index of column  
        # d - ending index of column  

    a, c = 0, 0
    while (a < b and c < d): 
        # Print the first row from the remaining rows. 
        for i in range (c, d):
            matrix[a][i] = num
            num += 1
            
        a += 1
    
        # Print the last column from the remaining columns. 
        for j in range (a, b):
            matrix[j][d-1] = num
            num += 1
        d -= 1
    
        # Print the last row from the remaining rows. 
        if (a < b): 
            for i in range (d-1,c-1, -1):
                matrix[b-1][i] = num 
                num += 1
            b -= 1
    
        # Print the first column from the remaining columns. 
        if (c < d): 
            for i in range (b-1,a-1,-1): 
                matrix[i][c] = num 
                num += 1
            c += 1


    for i in range (0 , n):
        for j in range (0, n):
            value = matrix [i][j]
            if((value%11) == 0):
                points += 1
                location = "(" + str(i) + "," + str(j) + ")"
                points_location.append(location)
            elif( i == j == 0):
                points += 1
                location = "(" + str(i) + "," + str(j) + ")"
                points_location.append(location)

    for i in range (0 , n):
        for j in range (0,n):
            print(matrix[i][j], end=' ')
        print()

    print()
    print("Total Power points : " + str(points))
    print()

    for i in range (0, len(points_location)):
        print(points_location[i])
        i += 1    

if (0 < n <= 100):
    chakravyuha(n)
    os.system('Pause')
else:
    exit()