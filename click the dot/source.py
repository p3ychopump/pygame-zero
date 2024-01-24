import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

left_time = 20
two_sec = 2         # 2초안에 점을 눌렀는지 판단
dots = []
lines = []

next_dot = 0

for dot in range(0, 10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

def draw():
    if((next_dot < 10) and (left_time > 0)):
        screen.fill("black")

        screen.draw.text('Time: ' + str(int(left_time)), color="white", midtop=(200, 10))
        number = 1

        for dot in dots:
            screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))            # pos[0]은 x좌표, pos[1]은 y좌표이다.
            dot.draw()
            number += 1

        for line in lines:
            screen.draw.line(line[0], line[1], (100, 0, 0))
    else:
        screen.fill("black")

        screen.draw.text('Game over', color="white", center=(200, 60), fontsize=60)
        screen.draw.text('Lift Time: ' + str(int(left_time)), color="white", center=(200, 100), fontsize=40)

def on_mouse_down(pos):
    global next_dot
    global lines
    global two_sec
    global left_time

    if((next_dot < 10) and (left_time > 0)):
        
        if(dots[next_dot].collidepoint(pos)):
            two_sec = 2                     # 점 클릭시 초 다시 시작
            if(next_dot):
                if(two_sec >= 0):           
                    left_time += 1          # 2초안에 클릭시 남은시간 1초 추가
                lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
            next_dot += 1
        else:
            lines = []
            next_dot = 0   
        
        
def update():
    global left_time
    global two_sec
    
    if((left_time > 0) and (next_dot < 10)):
        left_time -= 1 / 60     # 1/ 60은 1초를 의미한다.
        two_sec -= 1 / 60

pgzrun.go()