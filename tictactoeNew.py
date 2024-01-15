# Tictactoe also called Naughts and Crosses
# Computer will get smarter after it loses
# cells are numbered as follows:
# 1.2.3
# 4.5.6
# 7.8.9
# each game is stored as a sequence of 9 digits
# for example 563789... means human puts O in pos 5,
# computer puts X in position 6, etc
# human goes first
 
import turtle, time, random

turtle.setup(width=500, height=700)
turtle.color("black","white")
turtle.speed(0)
xc=40
yc=0
restartbtnx=-200
restartbtny=-260
exitbtnx=20
exitbtny=-260
lose = []
moves = ""
playermoves = [] 
computermoves = []
GameOver = False
computermove = False

def drawline(xstart,ystart,direction,mywidth,length):
    turtle.penup()
    turtle.width(mywidth)
    turtle.goto(xstart,ystart)
    turtle.setheading(direction)
    turtle.pendown()
    turtle.forward(length)
    
def drawfield():
 for i in range(2):
  drawline(xc-200,yc-100+i*100,0,7,300)
 for i in range(2):
  drawline(xc-100+i*100,yc-200,90,7,300)

def drawrect(topleftx,toplefty,width,height):
    drawline(topleftx,toplefty,0,2,width)
    drawline(topleftx+width,toplefty,270,2,height)
    drawline(topleftx+width,toplefty-height,180,2,width)
    drawline(topleftx,toplefty-height,90,2,height)


def drawbutton(topleftx,toplefty,name):
    turtle.penup()
    turtle.goto(topleftx+80,toplefty-54)
    turtle.write(name, font=("arial",20),align="center")
    drawrect(topleftx,toplefty,160,80)

def testrect(topleftx,toplefty,width,height,x,y):
    if (x >= topleftx) and (x <= topleftx+width):
        if (y <= toplefty) and (y >= toplefty-height):
            return True
    return False

def testbuttonclick(x,y):
    if testrect(restartbtnx,restartbtny,200,100,x,y):
        playagain()
    if testrect(exitbtnx,exitbtny,200,100,x,y):
        turtle.bye()

# Checking for GameOver should be done here
# (finding gameover in a nested function will still
# execute code in higher levels and cause errors)
def screenclick(x,y):
    global computermove, playermoves, GameOver, lose
    testbuttonclick(x,y)
    if GameOver: return
    squarenum = 0 # squarenum is the square 1...9 we clicked on
    if (x<0)and(x>-100):
        if (y<0) and (y>-100):
           squarenum = 5
        if (y>0) and (y <100):
           squarenum = 2
        if (y<-100) and (y > -200):
           squarenum = 8
    if (x<-100) and (x > -200):
        if (y<0) and (y>-100):
           squarenum = 4
        if (y>0) and (y <100):
           squarenum = 1
        if (y<-100) and (y > -200):
           squarenum = 7
    if (x<100) and (x > 0):
        if (y<0) and (y>-100):
           squarenum = 6
        if (y>0) and (y <100):
           squarenum = 3
        if (y<-100) and (y > -200):
           squarenum = 9
    if moves.find(str(squarenum)) > 0: return # this square is taken
    if squarenum == 0: return # outside bounds
    choose(squarenum) # humans choice
    if testwin(playermoves):
          endgame("Human Wins")
          lose.append(moves[:-1])
    elif len(moves) > 8:
          GameOver = True
          message("Draw")
    if not GameOver:
       computermove = True  
       docomputermove()
       if testwin(computermoves):
          message("Computer Wins")
          GameOver = True
       if len(moves) > 8:
          message("Draw")
          GameOver = True

def StartGame():
  turtle.tracer(False)
  turtle.clear()
  drawfield()
  message("Tic-Tac-Toe",y=300,size=30)
  message("Computer gets smarter after each game",y=290,size=14)
  message("Tap on any open cell to make your choice",y=270,size=14)
  message("Human = Circle",y=230,size=20)
  message("Computer = Square",y=200,size=20)
  drawbutton(restartbtnx,restartbtny,"Play Again")
  drawbutton(exitbtnx,exitbtny,"Exit")
  turtle.shapesize(3,3,8)
  turtle.penup()
  turtle.hideturtle()
  turtle.tracer(True)

def message(mystring,y=140,size=40):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,y)
    turtle.write(mystring, font=("arial",size),align="center")

def endgame(mymessage):
    global GameOver
    GameOver = True
    message(mymessage)

#draw next move on square 1,2,...,9
def choose(i):
    global computermoves, playermoves, moves
    moves=moves+str(i) 
    if computermove:
        turtle.shape("square")
        computermoves.append(i)
    else:
        turtle.shape("circle")
        playermoves.append(i)
    i=i-1 # use 0,1,2,...,8 for numbering squares when drawing 
    row = 2-(i // 3)
    col = i % 3
    turtle.goto(xc-150+col*100,yc-150+row*100)
    turtle.stamp()

def playagain():
    global GameOver, moves, playermoves, computermoves
    global computermove
    GameOver = False
    StartGame()
    moves = ""
    playermoves = []
    computermoves = []
    computermove = False
    
def docomputermove():
    global moves, computermove, computermoves, GameOver
    if GameOver: return
    availablemoves = [1,2,3,4,5,6,7,8,9]
    for i in moves:
        if int(i) in availablemoves:
          availablemoves.remove(int(i))
    x = availablemoves[0]
    foundnotlose = False
    for i in availablemoves:
        if not (moves+str(i) in lose):
            x=i
            foundnotlose = True
    if not foundnotlose:
        lose.append(moves[:-3])
    choose(x)
    computermove = False
    print("Moves = ", moves)
    
def check(a,b,c,mymoves):
    if (a in mymoves) and (b in mymoves) and (c in mymoves):
        return True
    else:
        return False

def testwin(mymoves):
    if check(1,2,3,mymoves): return True
    if check(4,5,6,mymoves): return True
    if check(7,8,9,mymoves): return True
    if check(1,4,7,mymoves): return True
    if check(2,5,8,mymoves): return True
    if check(3,6,9,mymoves): return True
    if check(1,5,9,mymoves): return True
    if check(3,5,7,mymoves): return True
    else:
        return False

# program starts here
turtle.onscreenclick(screenclick)
StartGame() 

