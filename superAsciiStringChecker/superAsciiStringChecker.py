 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-30 13:28:45
 ##

import os
import string

superAscii = True

def stringChecker(word):
    dict = {}
    newList = []
    letters = []
    
    
    def keyChecker(aLetter):
        key = 0
        for i in range (1, 27):
            if (dict.get(i) == aLetter):
                key = i
                break
    
        return key
        
    newList = list(string.ascii_lowercase)
    
    for i in range (1,27):
        dict[i] = newList[i-1]
        if (i==26):
            newList.clear()
            
    for i in range (1,27):
        confirm = dict[i] in word
        if (confirm == True):
            letters.append(dict[i])
    
    for letter in range (len(letters)):
        word.count(letters[letter])
        if (keyChecker(letters[letter]) != word.count(letters[letter])):
            
            global superAscii 
            superAscii= False
    
    
    print('Yes') if (superAscii == True) else print('No')

    
testCase = int(input())

strings = []

if(0 < testCase <= 100):
    for test in range (testCase):
        word = input()
        word = word.lower()
        if (0 < len(word) <= 400):
            strings.append(word)
    
    for i in range (testCase):
        stringChecker(strings[i])
        
    os.system('Pause')