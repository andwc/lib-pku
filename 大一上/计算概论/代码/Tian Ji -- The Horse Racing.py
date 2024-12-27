def main():
    while True:
        n=int(input())
        if n==0:
            exit()
        tianji=sorted(list(map(int,input().split())))
        king=sorted(list(map(int,input().split())))
        win,lose=0,0
        while True:
            if not tianji:
                break
            if tianji[-1]>king[-1]:
                win+=1
                del tianji[-1]
                del king[-1]
            elif tianji[-1]<king[-1]:
                lose+=1
                del tianji[0]
                del king[-1]
            elif tianji[-1]==king[-1]:
                if tianji[0]>king[0]:
                    del tianji[0]
                    del king[0]
                    win+=1
                else:
                    if tianji[0]<king[-1]:
                        lose+=1
                    del tianji[0]
                    del king[-1]
        print(200*(win-lose))
main()