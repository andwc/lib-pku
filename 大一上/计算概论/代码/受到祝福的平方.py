def cut(id):
    n=len(id)
    if n==0:
        j.append('oooooooo')
        return
    for i in range(n):
        if int(id[0:i+1]) in judge:
            iid=id[i+1:]
            cut(iid)
    return
id=str(input())
judge=[x**2 for x in range(1,31622)]
judge=set(judge)
j=[]
cut(id)
print('No' if not j else 'Yes')