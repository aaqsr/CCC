


needle=input()
hay = input()
foundH={}
n_freq={}
h_freq={}
count=0

for c in needle:
    n_freq[c]=n_freq.get(c,0)+1

for i in range(len(hay)-len(needle)+1):
    if i==0:
        for k in hay[:len(needle)]:
            h_freq[k]=h_freq.get(k,0)+1
    else:
        remove=hay[i-1]
        add=hay[i+len(needle)-1]
        h_freq[remove]-=1
        h_freq[add]=h_freq.get(add,0)+1
        if h_freq[remove]==0:
            h_freq.pop(remove)
    if h_freq==n_freq:
        val=str(hash(hay[i:i+len(needle)]))
        #val=hay[i:i+len(needle)]
        #print(val)
        if not(val in foundH):
            count+=1
            foundH[val]=True

print(count)
