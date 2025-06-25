def f(x):
    return x**3-5*x**2+10*x-80
def f1(x):
    return 3*x**2-10*x+10
a=5
while 1:
    b=a-f(a)/f1(a)
    if abs(f(b))<1e-9:
        print(f'{b:.9f}')
        #print(f(b),b)
        break
    a=b