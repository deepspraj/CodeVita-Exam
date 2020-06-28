##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-06-27 13:18:37
 # @modify date 2020-06-27 13:18:37
##


import math
import os


num = int(input())
num = math.factorial(num)
expo =math.exp(1)

temp = float(num)/float(expo)
ans =round(temp)

print(ans)

os.system("Pause")
