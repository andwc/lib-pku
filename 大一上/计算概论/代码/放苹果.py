case=int(input())
def solve(apple,plate,e):
    ans=0
    if plate==1 or apple==0:
        return 1
    start=apple//plate if apple%plate==0 else apple//plate+1
    for i in range(start,min(apple+1,e+1)):
        ans+=solve(apple-i,plate-1,i)
    return ans
for _ in range(case):
    apple,plate=map(int,input().split())
    ans=solve(apple,plate,apple)
    print(ans)