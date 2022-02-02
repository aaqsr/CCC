# Take inputs

a = []

for i in range(0, 52):
    a.append(input())

# Algo

turns = 52
high_cards = ['ace', 'king', 'queen', 'jack']
score = [0, 0] #A, B

def player(arr, m, s):
    
    x = ""
    
    if (m % 2) == 0 or m == 0: #A scores
        arr[0] += s
        x = "A"
    else:
        arr[1] += s
        x = "B"

    print("Player {0} scores {1} point(s).".format(x, s))
        

for c in range(0, 51):
    
    turns = turns-1
    card = a[c]
    next1 = False
    next2 = False
    next3 = False
    next4 = False

    if c != 51:
        if not(a[c+1] in high_cards):
            next1 = True
            if c+2 < 52 and not(a[c+2] in high_cards):
                next2 = True
                if c+3 < 52 and not(a[c+3] in high_cards):
                    next3 = True
                    if c+4 < 52 and not(a[c+4] in high_cards):
                        next4 = True
    
    if card == "ace" and turns >= 4 and next4 == True:
        player(score, c, 4)
        
    if card == "king" and turns >= 3 and next3 == True:
        player(score, c, 3)

    if card == "queen" and turns >= 2 and next2 == True:
        player(score, c, 2)

    if card == "jack" and turns >= 1 and next1 == True:
        player(score, c, 1)

print("Player A: {0} point(s).\nPlayer B: {1} point(s).".format(score[0], score[1]))





























    
    
