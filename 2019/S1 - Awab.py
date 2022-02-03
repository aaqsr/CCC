def flipCounter(str):
    hori = str.count("H") % 2
    vert = str.count("V") % 2
    return (hori, vert)

# def horiFlip(table):
#     ansTable = []
    
#     for i in range(2):
#         tableRow = []
#         for j in range(2):
#             tableRow.append(table[j][i])
#         ansTable.append(tableRow)
            
#     return ansTable

# def vertFlip(table):
#     ansTable = table
#     return ansTable

def output(table):
    for i in range(2):
        for j in range(2):
            print(table[i][j], end=" ")
        print()

table = [
    [1, 2],
    [3, 4]
]
    
hori, vert = flipCounter(input())

if hori == 1 and vert == 1:
    output([
        [4, 3],
        [2, 1]
    ])
elif hori == 1:
    output([
        [3, 4],
        [1, 2]
    ])
elif vert == 1:
    output([
        [2, 1],
        [4, 3]
    ])
else:
    output(table)
