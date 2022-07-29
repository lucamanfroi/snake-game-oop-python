from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.current_score = 0
        self.penup()
        self.goto(0, 270)

    def refresh(self):
        self.clear()
        self.write(arg=f'Score: {self.current_score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)

