from turtle import Turtle
import time
up = 90
down = 270
right = 0
left = 180

class Snake:
    
    def __init__(self) -> None:
        self.segment = []
        self.start_pos = [(0,0),(-20,0),(-40,0)]
        pass    
        
    def createsnake(self):
        for x in self.start_pos:
            self.add_segment(x)

    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            new_x=self.segment[seg_num-1].xcor()   
            new_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.segment[0].forward(20)

    def up(self):
        if self.segment[0].heading() != down:
            self.segment[0].setheading(up)
  
    def left(self):
        if self.segment[0].heading() != right:
            self.segment[0].setheading(left)

    def right(self):
        if self.segment[0].heading() != left:
            self.segment[0].setheading(right)

    def down(self):
        if self.segment[0].heading() != up:
            self.segment[0].setheading(down)
    
    def add_segment(self,x):
            self.new_segment = Turtle('square')
            self.new_segment.color('white')
            self.new_segment.penup()
            self.new_segment.goto(x)
            self.segment.append(self.new_segment)
    
    def extend(self):
        self.start_pos.append(self.segment[-1].position())
        self.add_segment(self.segment[-1].position())
    