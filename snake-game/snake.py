from turtle import Turtle


class Snake:
    def __init__(self):
        self.turtles = []
        self.position = [(-40,0), (-20,0), (0,0)]
        self.create_snake()
        self.head = self.turtles[-1]
        
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
        
    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto[self.turtles[0].pos()]
        self.turtles.insert(0,new_segment)
        
    def up(self):
        self.head.setheading(90)
    
    def down(self):
        self.head.setheading(279)
        
    def right(self):
        self.head.setheading(0)
    
    def left(self):
        self.head.setheading(180)
        