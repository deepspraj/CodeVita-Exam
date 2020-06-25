import math
import os


num = int(input())
num = math.factorial(num)
expo =math.exp(1)

temp = float(num)/float(expo)
ans =round(temp)

print(ans)

os.system("Pause")
