def main():
    n=int(input())
    num=list(map(int,input().split()))
    ans=0
    if n==1:
        print(1)
        exit()
    else:
        k=0
        try:
            while num[k]==num[k+1]:
                k+=1
        except IndexError:
            print(1)
            exit()
        judge=sgn(num[k],num[k+1])
        ans+=2
        current=num[k+1]
        for i in range(k+2,n):
            if num[i]==current:
                continue
            if judge>0:
                if num[i]>current:
                    current=num[i]
                    continue
                elif num[i]<current:
                    current=num[i]
                    judge=-1
                    ans+=1
                    continue
            elif judge<0:
                if num[i]>current:
                    current=num[i]
                    judge=1
                    ans+=1
                    continue
                elif num[i]<current:
                    current=num[i]
                    continue
        print(ans)
def sgn(a,b):
    if a>b:
        return -1
    elif a<b:
        return 1
main()