num=int(input())
a=0
for j in range(num):
    shuru = input()
    answer = 0
    check = 0
    check1 = 0
    for i in range(2, len(shuru)):
        if check1 > 0:
            check1 -= 1
            continue
        if shuru[i] == shuru[i - 1] == shuru[i - 2] == '#' and check == 0:
            check = 1
            answer += 1
        elif shuru[i] == shuru[i - 1] == shuru[i - 2] == '#' and check == 1:
            if i + 4 >= len(shuru):
                check = 0
            elif shuru[i + 2] == shuru[i + 3] == shuru[i + 4] == '#':
                check = 1
                check1 = 4
            else:
                check = 0
    a+=answer
print(a)