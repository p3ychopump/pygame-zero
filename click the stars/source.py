import pgzrun
import random

FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
COLORS = ["green", "blue"]

game_over = False
game_complete = False
current_level = 1
stars = []
animations = []

mode = ""

easy = Actor("easy")
easy.x = 267
easy.y = HEIGHT / 2

hard = Actor("hard")
hard.x = 534
hard.y = HEIGHT / 2



def draw() :
    global stars, current_level, game_over, game_complete
    screen.clear()
    screen.blit("space", (0, 0))


    if(game_over) :
        display_massage("GAME OVER!", "Try again")
    elif(game_complete) :
        display_massage("YOU WON!", "Well done")
    else :
        if(mode == ""):
            easy.draw()
            hard.draw()
        else :
            for star in stars :
                star.draw()
    
def update() :
    global stars, game_complete, game_over, current_level, stars, animations, mode

    if((mode == "easy") or (mode == "hard")) :
        if(len(stars) == 0) :
            stars = make_stars(current_level)

    if((game_over) or (game_complete)) :
        if(keyboard.K_RETURN):
            game_over = False
            game_complete = False
            current_level = 1
            stars = []
            stop_animations(animations)
            animations = []
            mode = ""


def make_stars(number_of_extra_stars) :
    colors_to_create = get_colors_to_create(number_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colors_to_create(number_of_extra_stars) :
    colors_to_create = ["red"]
    for i in range(0, number_of_extra_stars) :
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create


def create_stars(colors_to_create) :
    new_stars = []
    for color in colors_to_create :
        star = Actor(color + "-star")
        new_stars.append(star)
    return new_stars


# 별들의 위치를 잡는 함수
def layout_stars(stars_to_layout) :
    number_of_gaps = len(stars_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(stars_to_layout)
    for index, star in enumerate(stars_to_layout) :         # enumerate(리스트)함수는 인덱스번호와 값을 리턴하기 때문에 
                                                            # 변수 2개로(index, star)받아야 함
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos
        # print(star.x)
        if(mode == "hard"):
            if(random.randint(1, 2) == 1) :
                star.y = HEIGHT - 43                # -43을 안하고 실행을 하면 이미지에 중간을 기준으로 만들어져서 반이 짤림 그래서 잘린만큼 올려줌


def animate_stars(stars_to_animate) :
    for star in stars_to_animate :
        duration = START_SPEED - current_level
        star.anchor = ("center", "bottom")
        if(star.y == 85) :                          # 별이 위에서 생성되었을 때 아래로 내려가게
            animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        else :                                      # 별이 아래서 생성되었을 떄 위로 올라가게
            animation = animate(star, duration=duration, on_finished=handle_game_over, y=0 + 85)
        animations.append(animation)
    


def handle_game_over() :
    global game_over
    game_over = True


def on_mouse_down(pos) :
    global stars, current_level, mode, START_SPEED
    for star in stars :
        if(star.collidepoint(pos)) :
            if("red" in star.image):
                red_star_click()
            else:
                handle_game_over()

    
    if(easy.collidepoint(pos)):
        mode = "easy"
        START_SPEED = 10
    elif(hard.collidepoint(pos)) :
        mode = "hard"
        START_SPEED = 7

    

def red_star_click():
    global current_level, stars, animations, game_complete
    stop_animations(animations)
    if(current_level == FINAL_LEVEL) :
        game_complete = True
    else:
        current_level = current_level + 1
        stars = []
        animations = []


def stop_animations(animations_to_stop) :
    for animation in animations_to_stop:
        if(animation.running) :
            animation.stop()


def display_massage(heading_text, sub_heading_text) :
    screen.draw.text(heading_text, fontsize = 60, center = CENTER, color = FONT_COLOR)
    screen.draw.text(sub_heading_text, fontsize = 30, center = (CENTER_X, CENTER_Y + 30), color = FONT_COLOR)
    screen.draw.text("-Press the enter key to retry-", fontsize = 30, center = (CENTER_X, CENTER_Y + 60), color = FONT_COLOR)






pgzrun.go()