num=int(input())
a,answer=0,0
while 5**a<=num:
    a+=1
for i in range(1,a):
    answer+=num//(5**i)
print(answer)