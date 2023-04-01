import csv 

def getRow(a):
    l = len(a)
    for r in range(l):
        if (r!= 0 and a[r] > 2):
            return r
    return 0

def trecimalToDecimal(a, f):
    sum = 0
    if (not f):
        for i in range (1,len(a)):
            sum += 3**(i-1) * a[i]
            # sum += 3**(1) * a[i]
        return sum
    else:
        for i in range(1, len(a)):
            sum += 3**(len(a)-1-i) * a[i]
        return sum

jump = []
temp = 0
def playGame(n):
    global temp
    arr = [0, n]
    nextRow = getRow(arr)
    step = 0
    while (nextRow != 0):
        arr[nextRow] = arr[nextRow] - 3
        if (nextRow + 1 == len(arr)):
            arr.append(1)
        else:
            arr[nextRow + 1] = arr[nextRow + 1] + 1
        arr[nextRow - 1] = arr[nextRow - 1] + 2
        # print(arr)
        nextRow = getRow(arr)
        step=step+1
    
    # diff = trecimalToDecimal(arr, 0) - n
    diff = trecimalToDecimal(arr, 0) - temp
    if (diff != 1):
        jump.append((n,diff))
    
    print ("n: ", n, end=" ")
    print ("| h: ", len(arr) - 1, end=" ")
    print ("| arr: ", arr, end = " ")
    print ("| trec: ", trecimalToDecimal(arr, 0), end = " ")
    print ("| diff: ",  trecimalToDecimal(arr, 0) - temp)
    # print ("| steps: ",  step)

    temp = trecimalToDecimal(arr, 0)

def playGameStepByStep (n):
    global temp
    arr = [0, n]
    nextRow = getRow(arr)
    step = 0 
    
    print ("n = ", n) 
    while (nextRow != 0):
        print ("step: ", step, end = " ")
        print (" | arr: ", arr, end = " ")
        print ("trec: ", trecimalToDecimal(arr, 0))
        arr[nextRow] = arr[nextRow] - 3
        if (nextRow + 1 == len(arr)):
            arr.append(1)
        else:
            arr[nextRow + 1] = arr[nextRow + 1] + 1
        arr[nextRow - 1] = arr[nextRow - 1] + 2
        nextRow = getRow(arr)
        step = step + 1

    print ("step: ", step, end = " ")
    print (" | arr: ", arr, end = " ")
    print ("trec: ", trecimalToDecimal(arr, 0))
    print (" ")

for i in range(1,200):
   playGame(i)

# for i in range(215,216):
#    playGameStepByStep(i)

# playGameStepByStep(20)

# with open ('testing.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     for p in jump:
#         writer.writerow([p[0],p[1]])

# for num in jump:
#     print (num[1], end = "")
#     print (", ", end = "")
