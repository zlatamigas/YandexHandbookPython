n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

a2 = int((k1 * n - m * n) / float(k1 - k2))
a1 = n - a2

print(a1, a2)
