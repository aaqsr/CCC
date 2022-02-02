from distutils.command.install_scripts import install_scripts


def count(inStr):
    charDict={}
    for c in inStr:
        charDict[c]=charDict.get(c,0)+1
    return charDict

def comp(Dict1,Dict2):
    rflag = True
    for k in Dict2.keys():
        if k != "*":
            if Dict2[k] > Dict1.get(k,0):
                rflag = False
                break
    return rflag


CharDict1 = count(input())
CharDict2 = count(input())

if comp(CharDict1,CharDict2):
    print("A")
else:
    print("N")
