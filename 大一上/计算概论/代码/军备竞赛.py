money=int(input())
l=list( map( int,input().split() ) )
wo,di=0,0
while l:
    xiao=min(l)
    da=max(l)
    if money>=xiao:
        money-=xiao
        wo+=1
        l.remove(xiao)
    elif wo>di and money<xiao and len(l)!=1:
        money+=da
        di+=1
        l.remove(da)
    else:
        break
print(wo-di)