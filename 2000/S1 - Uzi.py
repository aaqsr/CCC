# Take inputs

print("How many quarters does Martha have in the jar?")
q = int(input())
print("How many times has the first machine been played since paying out?")
m1 = int(input())
print("How many times has the second machine been played since paying out?")
m2 = int(input())
print("How many times has the third machine been played since paying out?")
m3 = int(input())

# Algo

#She plays m1 then m2 then m3

count = 0

while q != 0:
    q -= 1
    count += 1

    if count % 3 == 0: # Plays m3
        if m3 == 10:
            q += 9
            m3 = 0
        else:
            m3 += 1
    elif count % 2 == 0: # Plays m2
        if m2 == 100:
            q += 60
            m2 = 0
        else:
            m2 += 1
    else: # Plays m1
        if m1 == 35:
            q += 30
            m1 = 0
        else:
            m1 += 1
    

print("Martha plays {0} times before going broke.".format(count))
