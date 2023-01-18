n = input()
p, v, t = map(int, input().split())
count = 0
for i in range(int(n)):
    p, v, t = map(int, input().split())
    if p + v + t >= 2:
        count += 1
print(count)