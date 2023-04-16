def display(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j]==True):
                print('Q',end=' ')
            else:
                print('X',end=' ')
        print('\n')
def issafe(row,col,board):
    # print(row,col)
    for i in range(row):
        if(board[i][col]==True):
            return False
    #left diag
    left=min(row,col)
    for i in range(1,left+1):
        if(board[row-i][col-i]==True):
            return False
        #right diag
    right=min(row,len(board[0])-1-col)
    for i in range(1,right+1):
        if(board[row-i][col+i]==True):
            return False
    # print(left,right,"_______")
    return True
def nqueens(row,board):
    if(row==len(board)):
        display(board)
        print("\n")
        return 1
    count=0
    for col in range(len(board[0])):
        if issafe(row,col,board):
            board[row][col]=True
            count+=nqueens(row+1,board)
            board[row][col]=False
    return count
n=int(input())
board=[[False]*n for x in range(n)]
print(nqueens(0,board))