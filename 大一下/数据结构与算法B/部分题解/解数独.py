class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        row=[[False]*10 for _ in range(9)]
        col=[[False]*10 for _ in range(9)]
        block=[[False]*10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num=int(board[i][j])
                    row[i][num]=True
                    col[j][num]=True
                    block[3*(i//3)+j//3][num]=True
        def slove(x,y,row,col,block,board,cnt,ans):
            if cnt==81:
                ans.append(board.copy())
                return
            if ans:
                return
            if board[x][y]=='.':
                for k in range(1,10):
                    if not row[x][k] and not col[y][k] and not block[3*(x//3)+y//3][k]:
                        row[x][k]=True
                        col[y][k]=True
                        block[x//3*3+y//3][k]=True
                        board[x][y]=str(k)
                        if y!=8:
                            slove(x,y+1,row,col,block,board,cnt+1,ans)
                        else:
                            slove(x+1,0,row,col,block,board,cnt+1,ans)
                        if ans:
                            return
                        row[x][k]=False
                        col[y][k]=False
                        block[x//3*3+y//3][k]=False
                        board[x][y]='.'
            else:
                if y!=8:
                    slove(x,y+1,row,col,block,board,cnt+1,ans)
                else:
                    slove(x+1,0,row,col,block,board,cnt+1,ans)
                if ans:
                    return
            return
        ans=[]
        slove(0,0,row,col,block,board,0,ans)
board=[]
for i in range(9):
    s=list(input())
    board.append(s)
Solution().solveSudoku(board)
for i in board:
    print(i)