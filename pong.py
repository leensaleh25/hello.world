#import turtle module
import turtle
wind=turtle.Screen() # intialize screen
wind.title('ping bong by leen') #set the title of tj=he window
wind.bgcolor('black') # set the background color of the window 
wind.setup(width=800,height=600)# set hight and width of the window
wind.tracer(0) #stops the window from updating automatically

# paddle1
paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape('square')
paddle1.color('white')
paddle1.shapesize(stretch_wid=5 ,stretch_len=1)
paddle1.penup() #stops the object from drowing lines
paddle1.goto(-350,0) # set the position of the object

#paddle2
paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape('square')
paddle2.color('white')
paddle2.shapesize(stretch_wid=5 ,stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)
#ball
ball=turtle.Turtle()
ball.speed(9)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=-0.2

#score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color('red')
score.penup()
score.hideturtle()
score.goto(0,260)


# functions 1
def paddle1_up():
    y=paddle1.ycor()
    y+=20
    paddle1.sety(y)

def paddle1_down():
    y=paddle1.ycor()
    y-=20
    paddle1.sety(y)


# functions2
def paddle2_up():
    y=paddle2.ycor() # get the y coordinate of the madrab2
    y+=20
    paddle2.sety(y)

def paddle2_down():
    y=paddle2.ycor()
    y-=20
    paddle2.sety(y)

#keyboard bindlings
wind.listen() # tell the window to expect keyboard input 
wind.onkeypress(paddle1_up,'w')
wind.onkeypress(paddle1_down,'s')
wind.onkeypress(paddle2_up,'Up')
wind.onkeypress(paddle2_down,'Down')    
# main game loop
while True:
    wind.update() # updates the screen everytime the loop run

     #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
       
    if ball.ycor() < -290:
        ball.sety(-290)
        
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1 
        score1+=1
        score.clear()
        score.write('player A: {} player B: {}'.format(score1,score2),align='center' ,font=('center',24,'normal'))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2+=1
        score.clear()
        score.write('player A: {} player B: {}'.format(score1,score2),align='center' ,font=('center',24,'normal'))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1