n = int(input())
m = int(input())
t = int(input())
curr_t = n * 60 + m + t

tn = curr_t // 60
wn = tn % 24
wm = (curr_t - tn * 60) % 60
print(f'{wn:0>2}:{wm:0>2}')
