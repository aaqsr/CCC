# Take inputs

N = int(input())
b = []

for n in range(N):
    b.append(list(map(int, input().split())))

for B in b:
    ans = "No"

    if 2007 - B[0] > 18:
        ans = "Yes"
    elif 2007 - B[0] == 18:
        if B[1] < 2:
            ans = "Yes"
        elif B[1] == 2:
            if B[2] <= 27:
                ans = "Yes"

    print(ans)
