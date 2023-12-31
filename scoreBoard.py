from turtle import Turtle

ALIGN = "center"
FONT = ("Courier",24,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.update_sb()


    def game_over(self):

        self.goto(0,0)
        self.write("Game Over", align=ALIGN, font=FONT)

    def update_sb(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):

        self.score+=1
        self.clear()
        self.update_sb()