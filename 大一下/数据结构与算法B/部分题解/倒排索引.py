n=int(input())
word=[None]*n
for i in range(n):
    word[i]=set(input().split())
m=int(input())
for i in range(m):
    target=input()
    judge=0
    for j in range(n):
        if target in word[j]:
            print(j+1,end=' ')
            judge+=1
    if judge==0:
        print('NOT FOUND')
    else:
        print()

