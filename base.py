import turtle
import time
import random

# initailizing scores
score = 0
hscore = 0 
delay = 0.1

# creating window
gwdw = turtle.Screen()
gwdw.setup(1280,720)
gwdw.title("SNAKE")
gwdw.bgcolor("black")
gwdw.tracer(0)

# creating the snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0,0)
snake.direction = "Stop"

# creating snake food
food = turtle.Turtle()
colors = random.choice(['red','green','yellow','orange','pink','white'])
food.speed(0)
food.shape("circle")
food.color(colors)
food.penup()
food.goto(0,100)

# displaying scores
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0 | High Score : 0", align="center",font=('arial',20,'bold'))

# directions
def directionup():
    if snake.direction != "down":
        snake.direction = "up"

def directiondown():
    if snake.direction != "up":
        snake.direction = "down"

def directionleft():
    if snake.direction != "right":
        snake.direction = "left"

def directionright():
    if snake.direction != "left":
        snake.direction = "right"

# movement 
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+20)

# assigning keys for movement
gwdw.listen()
gwdw.onkeypress(directionup, "w")
gwdw.onkeypress(directiondown, "s")
gwdw.onkeypress(directionleft, "a")
gwdw.onkeypress(directionright, "d")


grow = []

# Gameplay
while True:
    gwdw.update()

    #check collisions  
    if snake.xcor() > 590 or snake.xcor() < -590 or snake.ycor() > 590 or snake.ycor() < -590:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "Stop"
        colors = random.choice(['red','green','yellow','orange','pink','white'])
        shapes = random.choice(['square', 'circle'])
        
        # collision with body
        for segment in grow:
            segment.goto(1000, 1000)
        grow.clear()
        score = 0
        delay = 0.1
        pen.clear()
        #score updation
        pen.write("Score : {} | High Score : {} ".format(
            score, hscore), align="center", font=("candara", 24, "bold"))

    #eating food  
    if snake.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        colors = random.choice(['red','green','yellow','orange','cyan','white'])
        food.color(colors) 
        # growing body
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        tcolors = random.choice(['red','green','yellow','orange','pink','white'])
        body.color(tcolors)  
        body.penup()
        grow.append(body)
        delay -= 0.001
        score += 10
        if score > hscore:
            hscore = score
        pen.clear()
        pen.write("Score : {} | High Score : {} ".format(
            score, hscore), align="center", font=("candara", 24, "bold"))
    
    # Checking for snake collisions with body
    for index in range(len(grow)-1, 0, -1):
        x = grow[index-1].xcor()
        y = grow[index-1].ycor()
        grow[index].goto(x, y)
    if len(grow) > 0:
        x = snake.xcor()
        y = snake.ycor()
        grow[0].goto(x, y)
    move()
    for segment in grow:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in grow:
                segment.goto(1000, 1000)
            grow.clear()
 
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} | High Score : {} ".format(
                score, hscore), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
