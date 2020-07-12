n = int(input())

def numberCalculate(n):
    lists = [6,28,66,120]

    totalCount = 0
    for i in range (1,n+1):
        totalCount += i

    for i in range (0, totalCount-4):
        newNumber = (lists[i+3] - lists[i+2])*3 + lists[i+1]
        if (newNumber >100000):
            break
        lists.append(newNumber)
        
    lists = list(map(str,lists))

    for i in range (0,len(lists)):
        if (len(lists[i])==1):
            new = str(0) + str(0) + str(0) + str(0) + lists[i]
            lists[i] = new
        elif (len(lists[i])==2):
            new = str(0) + str(0) + str(0) + lists[i]
            lists[i] = new
        elif (len(lists[i])==3):
            new = str(0) + str(0) + lists[i]
            lists[i] = new
        elif (len(lists[i])==4):
            new = str(0) + lists[i]
            lists[i] = new

    a = lineCount = 0
    rows = n+1
    for i in range(1, rows+1):
        k = 0
        for j in range(1, (rows-i)+1):
            print(end=" ")
        while (k != (i-1)):
            print(lists[a], end=" ")
            k = k + 1
            a = a + 1
        print()
        if (lineCount == n):
            exit()
        lineCount += 1

if (0<n<15):
    numberCalculate(n)
    