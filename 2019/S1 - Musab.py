inStr=input()
VCount=inStr.count("V")
HCount=len(inStr)-VCount
VCount %= 2
HCount %= 2
HVCase=(HCount,VCount)

if HVCase==(0,0):
    print("1 2")
    print("3 4")
elif HVCase==(1,1):
    print("4 3")
    print("2 1")
elif HVCase==(0,1):
    print("2 1")
    print("4 3")
elif HVCase==(1,0):
    print("3 4")
    print("1 2")