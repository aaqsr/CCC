# Take inputs

N = int(input())

sentence = ""

for i in range(N):
    s = []
    v = []
    o = []
    
    subjects = int(input())
    verbs = int(input())
    objects = int(input())

    for j in range(subjects):
        s.append(input())
    for p in range(verbs):
        v.append(input())
    for q in range(objects):
        o.append(input())

    # Sort arrays
    s.sort()
    v.sort()
    o.sort()

    for q in range(len(s)):
        for d in range(len(v)):
            for b in range(len(o)):
                sentence = "{0} {1} {2}.".format(s[q], v[d], o[b])
                print(sentence)

    print()

    
                
            

    


