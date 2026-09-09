n = int(input())
a = 0
b = 0
for _ in range(n):
    x = input().split()
    if x[-1] == "True":
        a += 1
    else:
        b += 1
print(a, b)
