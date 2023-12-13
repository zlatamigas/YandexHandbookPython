s1 = int(input())
s2 = int(input())
v1 = (s1 // 100 + s2 // 100) % 10
v2 = (s1 // 10 % 10 + s2 // 10 % 10) % 10
v3 = (s1 % 10 + s2 % 10) % 10

print(v1, v2, v3, sep='')
