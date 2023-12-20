import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
high_score = 0
play_time = 30

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200


def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if(game_over):
        screen.fill("pink")
        screen.draw.text("Best Score: " + str(high_score), bottomleft=(10, 40), fontsize=60)
        screen.draw.text("Final Score: " + str(score), topleft=(10, 40), fontsize=40)
        screen.draw.text("try again?", center=(WIDTH/2, HEIGHT/2), fontsize=60)
        screen.draw.text("press enter", center=(WIDTH/2, 250), fontsize=30)
        


def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))


def time_up():
    global game_over
    game_over = True


def update():
    global score, high_score
    global game_over                    # When changing the value of a variable outside a function, you must use global.

    if(game_over):
        if(keyboard.K_RETURN):
            game_over = False
            score = 0

            clock.schedule(time_up, play_time)
    else:
        if(keyboard.left):
            fox.x  = fox.x - 2
            if(fox.x < 62/2 ):          # If the x-coordinate of fox exceeds the left edge of the screen, 
                                        # it is fixed to the coordinate of the edge of the screen.
                fox.x = 62/2
        elif(keyboard.right):
            fox. x = fox.x + 2
            if(fox.x > WIDTH - 62/2):
                fox.x = WIDTH - 62/2

        if(keyboard.up):
            fox. y = fox.y - 2
            if(fox.y < 83/2):
                fox.y = 83/2
        elif(keyboard.down):
            fox. y = fox. y + 2
            if(fox.y > HEIGHT-83/2):
                fox.y = HEIGHT-83/2
        coin_collected = fox.colliderect(coin)

        if(coin_collected):
            score = score + 10
            place_coin()

        if(high_score < score):     # record breaking
            high_score = score


clock.schedule(time_up, play_time)       # Execute function after 30.0 seconds
place_coin()
pgzrun.go()