def quicksort(l):
    if len(l) <= 1:
        return l
    else:
        a=l[0]
        left=[x for x in l if x<a]
        m=[x for x in l if x==a]
        right=[x for x in l if x>a]
        return quicksort(left)+m+quicksort(right)
n=int(input())
l=list(map(int,input().split()))
l1=quicksort(l)
#print(l1)
answer=0.0
for i in range(len(l1)):
    p=l.index(l1[i])
    print(p+1,end=' ')
    l[p]=-1
    answer+=(n-i-1)*l1[i]
    #print(answer)
print()
answer/=n
print("{:.2f}".format(answer))
