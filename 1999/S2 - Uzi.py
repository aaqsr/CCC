# Take inputs

a = []

N = int(input())

for i in range(N):
    a.append(input())

#Search for formats

#f1 = dd/mm/yy
#f2 = yy.mm.dd
#f3 = Month, dd, yy

import re

for j in a:
    
    f1 = re.findall("\d\d/\d\d/\d\d", j)
    f2 = re.findall("\d\d.\d\d.\d\d", j)
    f3 = re.findall("[January|February|March|April|May|June|July|August|September|October|November|December]\s\d\d,\s\d\d", j)
    print(f3)
    
    #Replace f1s
    if len(f1) > 0:
        for i in range(0, len(f1)):

            c = f1[i][6:]
            d = "20"

            if int(c) > 24:
                d = "19"
            
            new = f1[i][:6] + "{0}{1}".format(d, c)

            j = j.replace(f1[i], new)


    #Replace f2s
    if len(f2) > 0:
        for i in range(0, len(f2)):

            e = f2[i][0:2]
            f = "20"

            if int(e) > 24:
                f = "19"
            
            new = "{0}{1}".format(f, e) + f2[i][2:]
            
            j = j.replace(f2[i], new)


    #Replace f3s
    if len(f3) > 0:
        for i in range(0, len(f3)):

            g = f3[i][-2:]
            h = "20"

            if int(g) > 24:
                h = "19"
            
            new = f3[i][:-2] + "{0}{1}".format(h, g)
            
            j = j.replace(f3[i], new)


    print(j)

            
