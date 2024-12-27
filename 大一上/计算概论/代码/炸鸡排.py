def main():
    n,k=map(int,input().split())
    t=list(map(float,input().split()))
    t.sort()
    if n==k:
        print("{:.3f}".format(min(t)))
        return
    s=0
    for i in range(0,n-k):
        s+=t[i]
    t[n-k]+=s
    ans=t[n-k]
    for i in range(1,1+k):
        if ans<t[n-k+i-1]:
            break
        ans=(t[n-k+i-1]+ans*(i-1))/(i)
    print("{:.3f}".format(ans))
main()