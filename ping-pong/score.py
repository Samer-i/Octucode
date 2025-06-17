from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
        
    def l_point(self):
        self.left_score +=1
        self.update_scoreboard()
        
    def r_point(self):
        self.right_score +=1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.left_score, align='center', font=("courier", 40, "normal"))
        self.goto(100,250)
        self.write(self.right_score, align='center', font=("courier", 40, "normal"))
        
        
        