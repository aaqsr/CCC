# Take inputs

b = int(input())
boxes = []

for B in range(b):
    boxes.append(list(map(int, input().split())))

# Sort boxes in order of volume

boxes.sort(key=lambda x: (x[0]*x[1]*x[2]))

i = int(input())
items = []

for I in range(i):
    items.append(list(map(int, input().split())))

for t in items:
    vol = t[0] * t[1] * t[2]
    ok = []

    for box in boxes:
        boxvol = box[0] * box[1] * box[2]
        if vol < boxvol:
            ok.append(box)

    if len(ok) > 0:
        # Check for length then width then height issues
        for o in ok:
            
            if t[0] > o[0]:
                if t[0] > o[2]:
                    ok.remove(o)

            if t[1] > o[1]:
                if t[1] > o[2]:
                    ok.remove(o)

            if t[2] > o[2]:
                if t[2] > o[0]:
                    ok.remove(o)
                    
        if len(ok) > 0:
            print(ok)
            print((ok[0][0] * ok[0][1] * ok[0][2]))
        else:
            print("Item does not fit.")
    else:
        print("Item does not fit.")
