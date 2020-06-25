import os
no_of_cases = int(input())
amount = []


def calculator(amount):
    no_of_fives = (amount-5)//5
    
    if ((amount - 5 * no_of_fives)%2 == 0):
        no_of_ones = 2 
    else:
        no_of_ones = 1
        
    no_of_twos = ((amount - 5 * no_of_fives) - no_of_ones )/2
    no_of_twos = int(no_of_twos)
    total_coins = (no_of_fives + no_of_twos + no_of_ones)
    print(total_coins,no_of_fives,no_of_twos,no_of_ones, end=" ")
    print("")
    
for i in range (0,no_of_cases):
    temp = int(input())
    amount.append(temp)

for i in range (0,no_of_cases):
    calculator(amount[i])
    
os.system("Pause")
