import os

num = int(input())
inputs = []


def coins_calculator(amount):
    no_of_tens = int(amount / 10) - 1
    if no_of_tens <= 0:
        no_of_tens = 0
    temp1 = int(amount / 5)
    if temp1 > 1:
        if temp1 % 2 == 0:
            no_of_fives = 1
        else:
            no_of_fives = 2
    else:
        no_of_fives = 0

    temp2 = int(amount - 10 * no_of_tens - 5 * no_of_fives)
    if temp2 % 2 == 0:
        no_of_ones = 2
    else:
        no_of_ones = 1

    no_of_twos = int(amount - 10 * no_of_tens - 5 * no_of_fives - 1 * no_of_ones) / 2
    total_coins = int(no_of_tens + no_of_fives + no_of_twos + no_of_ones)
    print(total_coins)


for i in range(0, num):
    temp = input()
    inputs.append(temp)

inputs = list(map(int, inputs))

for i in range(0, num):
    coins_calculator(inputs[i])

os.system("Pause")