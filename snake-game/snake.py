from turtle import Turtle


class Snake:
    def __init__(self):
        self.turtles = []
        self.position = [(-40,0), (-20,0), (0,0)]
        self.create_snake()
    def create_snake(self):
        for i in range(len(self.position)):
            new_turtule = Turtle("square")
            new_turtule.color("white")
            new_turtule.penup()
            new_turtule.goto(self.position[i])
            self.turtles.append(new_turtule)
            
    def move(self):
        for i in range(len(self.turtles) -1 ):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.turtles[-1].forward(20)
        
    def up(self):
        self.turtles[-1].setheading(90)
    
    def down(self):
        self.turtles[-1].setheading(279)
        
    def right(self):
        self.turtles[-1].setheading(0)
    
    def left(self):
        self.turtles[-1].setheading(180)
        