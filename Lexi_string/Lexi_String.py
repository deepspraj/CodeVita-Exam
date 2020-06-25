test_cases = int(input())
string_list = {}
word_list = {}
for case in range (0,test_cases):
    string_list[case+1] = input()
    word_list[case+1] = input()

def cal(user_word,string):
    word = []
    direct=[]
    sub_dict = {}
    
    for i in range (0,26):
        sub_dict[i+1] = string[i]
    
    for i in range (0,len(user_word)):
        temp1 = user_word[i]
        for j in range (0,26):
            temp2 = sub_dict[j+1]
            if (temp1 == temp2):
                word.append(j+1)
    
    word.sort()            
    for i in range (0,len(user_word)):
        temp = word[i]
        direct.append(sub_dict[temp])
        
    for i in range (0,len(direct)):
        print(direct[i],end="")
    print()

for result in range (0,test_cases):
    if (len(word_list[result+1])< 101 and len(string_list[result+1])<27 ):
        cal(word_list[result+1],string_list[result+1])
    else:
        print("ERRO")