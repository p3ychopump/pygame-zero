import pgzrun
from random import randint


time = 60
score = 0
apple = Actor("apple")


def draw():
    screen.clear()
    apple.draw()
    screen.draw.text("Score: " + str(score), color="white", topleft=(10, 10))
    screen.draw.text(str(int(time)), color="white", midtop=(400, 10))
    if(time<=0):
        screen.clear()
        screen.draw.text(str(score), color="white", center=(400, 300), fontsize=160)


def place_apple():
    apple.x = randint(10, 800)          # From 10 to 800 inclusive
    apple.y = randint(10, 600)


# mouse click event
def on_mouse_down(pos):
    global score

    if(apple.collidepoint(pos)):        # When I click on the apple 
        score += 10
        print("Good shot!")
        # print("score:",score)
        place_apple()
        
    else:
        print("You missed!")
        quit()                          # Ended


def update():
    global time

    time -= 1 / 60          # Decrease by 1 second


place_apple()
pgzrun.go()