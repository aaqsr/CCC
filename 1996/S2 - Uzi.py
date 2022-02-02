# Take inputs

N = int(input())
nums = []

for i in range(N):
    nums.append(input())

# Algo

def divby11(x):
    chars = []
    ans = "is not"
    final = ""
    
    for char in x:
        chars.append(char)
    
    while len(chars) > 2:
        new = ""
        extract = ""
        # Shorten chars
        extract = chars[-1]
        chars.pop()
        # Subtract extracted num from new chars
        for c in chars:
            new += c

        final = str((int(new) - int(extract)))

        chars = []
        
        for h in final:
            chars.append(h)

        print(final)

    if final == "11" or x == "11":
        ans = "is"

    print("The number {0} {1} divisble by 11".format(x, ans))     

    
# Output

for num in nums:
    divby11(num)
