from turtle import Screen , Turtle
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard


screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

turtle = Turtle()
scoreboard = ScoreBoard()
snake = Snake()
food = Food()
snake.createsnake()

screen.listen()
screen.onkey(snake.up,'w')
screen.onkey(snake.left,'a')
screen.onkey(snake.down,'s')    
screen.onkey(snake.right,'d')

screen.update()

game_stat = True

while game_stat:

    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.segment[0].distance(food) < 15:
        snake.extend()
        food.change()
        scoreboard.refresh()
        pass
    else:
        pass

    if snake.segment[0].xcor()>300 or snake.segment[0].xcor() < -300 or snake.segment[0].ycor()> 300 or snake.segment[0].ycor() < -300:
        turtle.hideturtle()
        turtle.penup()
        turtle.pencolor('white')
        turtle.write('Game over', align ='Center' , font = ('Courier',16,'normal'))
        game_stat = False
    else:
        pass

    for segment in snake.segment:
        if snake.segment[0] == segment:
            pass
        elif snake.segment[0].distance(segment) < 10:
            turtle.hideturtle()
            turtle.penup()
            turtle.pencolor('white')
            turtle.write('Game over', align ='Center' , font = ('Courier',16,'normal'))
            game_stat = False



screen.exitonclick()