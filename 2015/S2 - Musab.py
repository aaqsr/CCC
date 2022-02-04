def giveJersey(num, size):
    shirts=["S","M","L"]
    global jerseys
    if jerseys[num] in shirts[shirts.index(size):]:
        jerseys[num]="X"
        return True
    else:
        return False

def takeInp():
    j=int(input())
    a=int(input())
    global jerseys
    satisfied=0

    for i in range(j):
        jerseys[i+1]=input()

    for i in range(a):
        size,num = input().split()
        if giveJersey(int(num),size):
            satisfied+=1
    print(satisfied)

jerseys={}
takeInp()