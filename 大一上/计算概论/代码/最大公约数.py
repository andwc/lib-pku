import sys
for line in sys.stdin:
    try:
        #print(line)
        shuru=line.split()
        answer=1
        a=int(shuru[0])
        b=int(shuru[1])
        s=min(a,b)
        #print(a,b,s)
        for i in range(1,s+1):
            if a%i==0 and b%i==0:
                answer=i
        print(answer)
    except ValueError:
        continue
