from graphics import *

b = [[0 for i in range(6)] for j in range(10)] 

win = GraphWin("Chain Reaction",600,1000)
win.setBackground("black")


def checkBoard( x, y, t):
    if((x==0 or x==9) and (y==0 or y==5)):
        if(b[x][y]==2*t):
            b[x][y]=0
            updateBoard(x,y,t)
        if(b[x][y]==3*t):
            b[x][y]=0
            updateBoard(x,y,t)
    elif((x==0 or x==9) or (y==0 or y==5)):
        if(b[x][y]==3*t):
            b[x][y]=0
            updateBoard(x,y,t)
        elif(b[x][y]==4*t):
            b[x][y]=1
            updateBoard(x,y,t)
    else:
        if(b[x][y]==4*t):
            b[x][y]=0
            updateBoard(x,y,t)
        elif(b[x][y]==5*t):
            b[x][y]=1
            updateBoard(x,y,t)

def updateBoard( x, y, t):
    if((x==0 or x==9) and (y==0 or y==5)):
        if(x==0 and y==0):
            same(0,1,t)
            same(1,0,t)
            checkBoard(0,1,t)
            checkBoard(1,0,t)
        if(x==0 and y==5):
            same(0,4,t)
            same(1,5,t)
            checkBoard(0,4,t)
            checkBoard(1,5,t)
        if(x==9 and y==0):
            same(9,1,t)
            same(8,0,t)
            checkBoard(9,1,t)
            checkBoard(8,0,t)
        if(x==9 and y==5):
            same(9,4,t)
            same(8,5,t)
            checkBoard(9,4,t)
            checkBoard(8,5,t)
    elif((x==0 or x==9) or (y==0 or y==5)):
        if(x==0):
            same(0,y-1,t)
            same(0,y+1,t)
            same(1,y,t)
            checkBoard(0,y-1,t)
            checkBoard(0,y+1,t)
            checkBoard(1,y,t)
        if(x==9):
            same(9,y-1,t)
            same(9,y+1,t)
            same(8,y,t)
            checkBoard(9,y-1,t)
            checkBoard(9,y+1,t)
            checkBoard(8,y,t)
        if(y==0):
            same(x-1,0,t)
            same(x+1,0,t)
            same(x,1,t)
            checkBoard(x-1,0,t)
            checkBoard(x+1,0,t)
            checkBoard(x,1,t)
        if(y==5):
            same(x-1,4,t)
            same(x+1,4,t)
            same(x,5)
            checkBoard(x-1,5,t)
            checkBoard(x+1,5,t)
            checkBoard(x,4,t)
    else:
        same(x-1,y,t)
        same(x+1,y,t)
        same(x,y-1,t)
        same(x,y+1,t)
        checkBoard(x-1,y,t)
        checkBoard(x+1,y,t)
        checkBoard(x,y+1,t)
        checkBoard(x,y-1,t)


def drawGola(x,y,n,color):
    cX=(x*80+50)+40
    cY=(y*80+50)+40
    re=Rectangle(Point(x*80+50+1,y*80+50+1),Point(x*80+50+78,y*80+50+78))
    re.setFill('black')
    re.draw(win)
    if(n==1):
        pt=Point(cX,cY)
        cr=Circle(pt,20)
        cr.setFill(color)
        cr.draw(win)
    elif(n==2):
        pt1=Point(cX-10,cY)
        cr1=Circle(pt1,20)
        cr1.setFill(color)
        cr1.draw(win)
        pt2=Point(cX+10,cY)
        cr2=Circle(pt2,20)
        cr2.setFill(color)
        cr2.draw(win)
    elif(n==3):
        pt1=Point(cX-10,cY-10)
        cr1=Circle(pt1,20)
        cr1.setFill(color)
        cr1.draw(win)
        pt2=Point(cX+10,cY-10)
        cr2=Circle(pt2,20)
        cr2.setFill(color)
        cr2.draw(win)
        pt3=Point(cX,cY)
        cr3=Circle(pt3,20)
        cr3.setFill(color)
        cr3.draw(win)

    
        
def displayGole():
    for i in range(10):
        for j in range(6):
            if(b[i][j]<0):
                color='green'
            else:
                color='red'
            drawGola(j,i,abs(b[i][j]),color)

def same(x,y,t):
    if(b[x][y]*t<0):
        b[x][y]=b[x][y]*-1
    b[x][y]+=t


def upgradeGrid(color,win):
    for x in range(7):
        pt1=Point(x*80+50,50)
        pt2=Point(x*80+50,10*80+50)
        ln=Line(pt1,pt2)
        ln.setOutline(color)
        ln.draw(win)

    for y in range(11):
        pt1=Point(50,y*80+50)
        pt2=Point(6*80+50,y*80+50)
        ln=Line(pt1,pt2)
        ln.setOutline(color)
        ln.draw(win)



def main():
    t=1
    while 1 :
        t=t*(-1)
        if t==1:
            color = 'red'
        else:
            color = 'green'
        upgradeGrid(color,win)
        pt=win.getMouse()
        ypt=int((pt.x-50)/80)
        xpt=int((pt.y-50)/80)
        print(xpt,ypt)
        if(b[xpt][ypt]*t>=0):
            b[xpt][ypt]=b[xpt][ypt]+t;
            checkBoard(xpt,ypt,t);
        else:
            print("Invalid Move !!")
            t=t*(-1)
        displayGole()
        print(t)
        for i in range(10):
            print(b[i])
    win.close()

main()  

