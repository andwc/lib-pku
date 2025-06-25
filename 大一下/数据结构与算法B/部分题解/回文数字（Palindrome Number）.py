while True:
    try:
        s=input()
        j=len(s)-1
        i=0
        while i<=j:
            if s[i]!=s[j]:
                print('NO')
                break
            i+=1
            j-=1
        else:
            print('YES')
    except EOFError:
        break