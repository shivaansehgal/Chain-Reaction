# I am Positive



def getScore(b):
    mscore=0
    hscore=0
    for i in range(10):
        for j in range(6):
            if b[i][j]>0:
                mscore+=b[i][j]
            else:
                hscore-=b[i][j]
    return mscore,hscore;


def minimax(board,depth ,alpha, beta,turn):
    if depth == 0:
        ms,hs=getScore(board)
        if hs==0:
            return 950,[-1,-1]
        return ms-hs,[-1,-1]
    elif turn:
        maxEval = -1000
        cd=[-1,-1]
        for num in range(60):
            y=int(num/10)
            x=num%10
            if(board[x][y]<0):
                continue
            newBoard = [[0 for i in range(6)] for j in range(10)] 
            for i in range(10):
                for j in range(6):
                    newBoard[i][j]=board[i][j]
            newBoard[x][y]+=1
            checkBoard(x,y,1,newBoard)
            eval,coo = minimax(newBoard, depth - 1, alpha, beta ,0)
            if eval>maxEval:
                maxEval=eval
                cd=[x,y]
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval,cd
    else:
        minEval = +1000
        cd=[-1,-1]
        for num in range(60):
            y=int(num/10)
            x=num%10
            if(board[x][y]>0):
                continue
            newBoard = [[0 for i in range(6)] for j in range(10)] 
            for i in range(10):
                for j in range(6):
                    newBoard[i][j]=board[i][j]
            newBoard[x][y]-=1
            checkBoard(x,y,-1,newBoard)
            eval,coo = minimax(newBoard, depth - 1, alpha, beta, 1)
            if eval<minEval:
                minEval=eval
                cd=[x,y]
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval,cd

def checkBoard( x, y, t,b):
    if((x==0 or x==9) and (y==0 or y==5)):
        if(b[x][y]==2*t):
            b[x][y]=0
            updateBoard(x,y,t,b)
        if(b[x][y]==3*t):
            b[x][y]=0
            updateBoard(x,y,t,b)
    elif((x==0 or x==9) or (y==0 or y==5)):
        if(b[x][y]==3*t):
            b[x][y]=0
            updateBoard(x,y,t,b)
        elif(b[x][y]==4*t):
            b[x][y]=1
            updateBoard(x,y,t,b)
    else:
        if(b[x][y]==4*t):
            b[x][y]=0
            updateBoard(x,y,t,b)
        elif(b[x][y]==5*t):
            b[x][y]=1
            updateBoard(x,y,t,b)
    return b

def same(x,y,t,b):
    if(b[x][y]*t<0):
        b[x][y]=b[x][y]*-1
    b[x][y]+=t


def updateBoard( x, y, t,b):
    if((x==0 or x==9) and (y==0 or y==5)):
        if(x==0 and y==0):
            same(0,1,t,b)
            same(1,0,t,b)
            checkBoard(0,1,t,b)
            checkBoard(1,0,t,b)
        if(x==0 and y==5):
            same(0,4,t,b)
            same(1,5,t,b)
            checkBoard(0,4,t,b)
            checkBoard(1,5,t,b)
        if(x==9 and y==0):
            same(9,1,t,b)
            same(8,0,t,b)
            checkBoard(9,1,t,b)
            checkBoard(8,0,t,b)
        if(x==9 and y==5):
            same(9,4,t,b)
            same(8,5,t,b)
            checkBoard(9,4,t,b)
            checkBoard(8,5,t,b)
    elif((x==0 or x==9) or (y==0 or y==5)):
        if(x==0):
            same(0,y-1,t,b)
            same(0,y+1,t,b)
            same(1,y,t,b)
            checkBoard(0,y-1,t,b)
            checkBoard(0,y+1,t,b)
            checkBoard(1,y,t,b)
        if(x==9):
            same(9,y-1,t,b)
            same(9,y+1,t,b)
            same(8,y,t,b)
            checkBoard(9,y-1,t,b)
            checkBoard(9,y+1,t,b)
            checkBoard(8,y,t,b)
        if(y==0):
            same(x-1,0,t,b)
            same(x+1,0,t,b)
            same(x,1,t,b)
            checkBoard(x-1,0,t,b)
            checkBoard(x+1,0,t,b)
            checkBoard(x,1,t,b)
        if(y==5):
            same(x-1,5,t,b)
            same(x+1,5,t,b)
            same(x,4,t,b)
            checkBoard(x-1,5,t,b)
            checkBoard(x+1,5,t,b)
            checkBoard(x,4,t,b)
    else:
        same(x-1,y,t,b)
        same(x+1,y,t,b)
        same(x,y-1,t,b)
        same(x,y+1,t,b)
        checkBoard(x-1,y,t,b)
        checkBoard(x+1,y,t,b)
        checkBoard(x,y+1,t,b)
        checkBoard(x,y-1,t,b)
