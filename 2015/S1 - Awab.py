def usrIn():
    K = int(input())
    
    numbers = []
    
    for i in range(K):
        numbers.append((int(input())))
        
    return K, numbers



def filterArray(K, numbers):
    ansArr = []

    for i in range(K):
        if numbers[i] == 0:
            ansArr.pop()
        else:
            ansArr.append(numbers[i])
    
    return ansArr

def sumArray(arr):
    sum = 0
    
    for val in arr:
        sum += val
        
    return sum

intK, numArr = usrIn()
ans = filterArray(intK, numArr)
print(sumArray(ans))