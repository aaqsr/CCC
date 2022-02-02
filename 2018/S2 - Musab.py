# def rotate(rotateOrder, Tab):
#     retTable=Tab
#     print(Tab)
#     if rotateOrder==1:
#         for r in range(len(Tab)):
#             for c in range(len(Tab)):
#                 print(c,r)
#                 retTable[r][c]=Tab[c][-r-1]
    
#     if rotateOrder==2:
#         for r in range(len(Tab)):
#             for c in range(len(Tab)):
#                 retTable[r][c]=Tab[-r-1][-c-1]

#     if rotateOrder==3:
#         for r in range(len(Tab)):
#             for c in range(len(Tab)):
#                 retTable[r][c]=Tab[c][-r-1]
    
#     return retTable

def rotate(table, order):
    newTab=[]
    for c in range(order):
        newRow=[]
        for r in range(order):
            newRow.append(table[r][-c-1])
        newTab.append(newRow)
    return newTab


def createTable(order):
    table=[]
    for i in range(order):
        table.append([int(x) for x in input().split()])
    return table

def display(DispTable):
    for r in DispTable:
        for c in r:
            print(c, end=" ")
        print()


order = int(input())
table=createTable(order)

while table[0][0]>table[0][1] or table[0][0]>table[1][0]:
    table=rotate(table, order)

display(table)


