vi = int(input())
c1 = vi // 1000
c2 = vi // 100 % 10
c3 = vi // 10 % 10
c4 = vi % 10

print(c2, c1, c4, c3, sep='')
