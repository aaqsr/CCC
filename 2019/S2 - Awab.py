from math import floor, sqrt

def checkPrime(n: int) -> bool:
    primality = True
    sqrtn = floor(sqrt(n)) 
    
    for i in range(2, sqrtn + 1):
        if n % i == 0:
            primality = False
            break
        
    return primality

def usrIn():
    numberOfCases = int(input())
    numbers = []
    
    for i in range(numberOfCases):
        numbers.append(int(input()))
        
    return numbers

def findUpperPrime(num):
    # num += 1 
    
    while checkPrime(num) != True:
        num += 1
    
    return num 

def findB(num, prime):
    B = 2 * num - prime
    return B

def findingAB(num, currentPointer):
    A = findUpperPrime(currentPointer)
    B = findB(num, A)
    
    if checkPrime(B) == True:
        return [A, B]

    return [A, findingAB(num, A+1)]
        

numbers = usrIn()

for num in numbers:
    [A, B] = findingAB(num, num + 1)
    print(f"{B} {A}")