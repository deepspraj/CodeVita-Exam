 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-02 19:12:32
 # @modify date 2020-07-02 19:12:32
 ##

import os

string = input()
changes = int(input())

def stringmaker(string,changes):
    string1 = ''
    sub_string = []
    for i in range (0, changes):
        direction , index = input().split(" ")
        index = int(index)
        direction = direction.upper()
        if (direction == 'L'):
            string1 = string1 + (string[(index)])
        else:
            string1 = string1 + (string[-(index)])

    length = len(string)
    count_of_substring = int(length/changes)
    count = 1
    a = 0
    b = changes
    for i in range (0, int(count_of_substring)):
        if(count < int(count_of_substring)):
            string_new = string[a:b]
            a = b
            b = (2 * changes)
        else:
            string_new = string[a:]
            
        sub_string.append(string_new)
        count += 1
    count_of_anagrams = 0
    for i in range (0,int(count_of_substring)):
        temp1 = sorted(string1)
        temp2 = sorted(sub_string[i])
        if((len(temp1) == len (temp2)) and (temp1 == temp2)):
           count_of_anagrams = count_of_anagrams + 1
    return count_of_anagrams


if ((0<len(string)<=30) and (0<changes<=10)):
    ans = stringmaker(string,changes)
    if(ans > 0):
        print('YES')
    else:
        print('NO')
    
    os.system('Pause')