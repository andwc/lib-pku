H,L,n=map(int,input().split())
v=list(map(int,input().split()))
v.sort()
t=L/v[len(v)//2]
h=H-5.0*t**2
print(f'{h:.2f}')