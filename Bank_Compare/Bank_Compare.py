 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-01 15:28:22
 # @modify date 2020-07-01 15:28:22
 ##


## Assuming that borrower borrows same amount of money in every slabs

import os 

principal = int(input())
tenure = int(input())

def emi_calcultor (principal,years,rate):
    factor =  pow(1+(rate/1200),(years*12))
    emi = (principal *(rate/1200))/(1 - (1/factor))
    return emi

def calculator(principal, tenure):
    interest_slabs_bank_a = interest_slabs_bank_b = []
    sum = [0 , 0]
    slabs_of_bank_a = int(input())
    for i in range (0 , slabs_of_bank_a):
        interest_slabs_bank_a = interest_slabs_bank_a + input().split(" ")

    slabs_of_bank_b = int(input())
    for i in range (0 , slabs_of_bank_b):
        interest_slabs_bank_b = interest_slabs_bank_b + input().split(" ")
    
    interest_slabs_bank_a = list(map(float,interest_slabs_bank_a))
    interest_slabs_bank_b = list(map(float,interest_slabs_bank_b))
    
    for i in range (0,2):
        if(i == 0):
            count = slabs_of_bank_a
            rater = interest_slabs_bank_a
        else:
            count = slabs_of_bank_b
            rater = interest_slabs_bank_b
        for j in range (0,count):
            temp = emi_calcultor(principal,rater[(2*j)],rater[(2*j)+1])
            sum[i] = sum[i] + temp
    return sum

emis = calculator(principal , tenure)  

if (emis[0]<emis[1]):
    print("Bank A")
else:
    print("Bank B")

os.system("Pause")