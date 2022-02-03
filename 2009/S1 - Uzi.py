a = int(input())
b = int(input())

count = 0

for n in range(a, b):

    if ((n ** 0.5) % 1) == 0:
        if (round((n ** (1/3)), 1) % 1) == 0:
            count += 1

print(count)
