def find(s):
    global p
    if p[s] == s:
        return s
    else:
        p[s] = find(p[s])
        return p[s]


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    p = [x for x in range(2 * n + 1)]
    for i in range(m):
        shuru = list(input().split())
        x, y = int(shuru[1]), int(shuru[2])
        if shuru[0] == 'A':
            if find(x) == find(y):
                print("In the same gang.")

            elif find(x) == find(n + y) or find(y) == find(n + x):
                print("In different gangs.")
            else:
                print('Not sure yet.')
        else:
            p[find(n + x)] = find(y)
            p[find(n + y)] = find(x)