#Take inputs
N = int(input())
a = []

for i in range(N):
    a.append(int(input()))

#Sort array

for j in range(1, len(a)):
    key = a[j]
    i = j - 1
    while i >= 0 and a[i] > key:
        a[i+1] = a[i]
        i=i-1
    a[i+1] = key

smallest = 1000000000
size = 0

#General Case
for k in range(1, len(a)-2):
    size = ((a[k+1] - a[k])/2) + ((a[k+2] - a[k+1])/2)
    if size <= smallest:
        smallest = size

print(format(float(smallest), ".1f"))
