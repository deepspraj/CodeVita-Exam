 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-18 14:57:07
 # @modify date 2020-07-18 15:14:53
 ##

def pairFinder(a,b,lst):
    count = 0
    temp1 = temp2 = temp3 = 0
    for i in range (a):
        temp1 += lst[i]
    
    for i in range (a+1,b):
        temp2 += lst[i]
        
    for i in range (b+1, len(lst)):
        temp3 += lst[i]
        
    if (temp1 == temp2 == temp3):
        print(f'Indices which form equi pair {a,b}.')
        print(f'Slices are {0,a-1}, {a+1, b-1}, {b+1, len(lst)-1}.')
        count += 1
    
    return count
    
lst = input().split(' ')
lst = list(map(int , lst))
default = 0

for i in range (len(lst)):
    for j in range (len(lst)):
        if (j > (i + 1)):
            default = pairFinder(i,j,lst)
if(default == 0):
     print('Array does not contain any equi pair')