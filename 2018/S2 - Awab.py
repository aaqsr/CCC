def rotate90(table):
    order = len(table[0]) - 1
    
    ansTable = []
    
    for i in range(order + 1):
        tableRow = []
        for j in range(order, -1, -1):
            tableRow.append(table[j][i])
        
        ansTable.append(tableRow)
    
    return ansTable

def usrIn():
    order = int(input())
    table = []
    
    for i in range(order):
        table.append([int(x) for x in input().split()])
    
    return table

def output(table):
    for val in table:
        for num in val:
            print(num, end= " ")
        print()

def checkTable(table):
    correct = True

    order = len(table[0])

    for i in range(order-1):
        for j in range(order-1):
            if i > order - 1 or j > order - 1:
                break
            
            if table[i][j] > table[i][j+1] or table[i][j] > table[i+1][j]:
                correct = False
                break
            
    return correct
        
    
# table = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

table = usrIn()

rotatedTable = table

while checkTable(rotatedTable) != True:
    rotatedTable = rotate90(table)

output(rotatedTable)