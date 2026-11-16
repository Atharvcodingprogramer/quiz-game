import pgzrun
WIDTH = 800
HEIGHT = 600
TITLE = "Quiz game" 

option1 = Rect(30,300,250,100)
option2 = Rect(360,300,250,100)
option3 = Rect(30,450,250,100)

def draw() :
   screen.draw.filled_rect(option1,"orange")
   screen.draw.filled_rect(option2,"orange")
   screen.draw.filled_rect(option3,"orange")


def update() :
    pass
pgzrun.go()