import os

no_of_row, no_of_col = map(int,input().split(" "))
matrix = []
my_dict = {}

def total_qualities(matrix,row,col,my_dict):
    count = temp = 0
    if(matrix[row][col]==1):
        for i in range (row -1 , row +2):
            for j in range (col -1, col +2 ):
                if(i>=0 and j>=0):
                    try:
                        if (i==row and j==col):
                            temp = 0
                        else:
                            temp = matrix[i][j]            
                    except:
                        temp = 0
                else:
                    temp = 0
                count = count + temp
        index = str(row+1) + ":" + str(col+1) + ":" + str(count)
        my_dict[index] = count

def calculator(no_of_row,no_of_col,matrix,my_dict):
    for i in range (0,no_of_row):
        arr = input().split(" ")
        arr = list(map(int,arr))
        matrix.append(arr)

    for row in range(0,no_of_row):
        for col in range (0,no_of_col):
            total_qualities(matrix,row,col,my_dict)
    
    ans = max(my_dict, key=my_dict.get)
    print(ans)


if ((0<no_of_row<100) and (0<no_of_col<100)):
    calculator(no_of_row,no_of_col,matrix,my_dict)
else:
    exit("Either Row or Column are out of scope")



    os.system("Pause")