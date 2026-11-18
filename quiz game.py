import pgzrun
WIDTH = 800
HEIGHT = 600
TITLE = "Quiz game" 

option1 = Rect(30,300,270,120)
option2 = Rect(345,300,270,120)
option3 = Rect(30,450,270,120)
option4 = Rect(345,450,270,120)
questionbox = Rect(30,75,582,200)
skipbox = Rect(650,300,120,270)
timerbox = Rect(650,75,122,200)

def draw() :
   screen.draw.filled_rect(option1,"dark orange")
   screen.draw.filled_rect(option2,"dark orange")
   screen.draw.filled_rect(option3,"dark orange")
   screen.draw.filled_rect(option4,"dark orange")
   screen.draw.filled_rect(questionbox,"dark blue")
   screen.draw.filled_rect(skipbox,"dark green")
   screen.draw.filled_rect(timerbox,"dark blue")


def update() :
    pass
pgzrun.go()