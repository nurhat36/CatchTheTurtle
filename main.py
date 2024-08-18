import random
import turtle
import schedule
import time

score = 0
time_left = 30

# Turtle kurulumları
board = turtle.Screen()
board.bgcolor("light blue")
board.title("Turtle")
board.screensize(500, 500)

t = turtle.Turtle()
t.penup()
t.shapesize(5)


def update_score(x, y):
    global score
    score += 1
    update_labels()

def update_labels():
    label_turtle.clear()
    label_turtle.goto(0, 290)
    label_turtle.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))
    label_turtle.goto(0, 270)
    label_turtle.write(f"Time Left: {time_left} seconds", align="center", font=("Arial", 16, "bold"))


def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        update_labels()
    else:
        schedule.clear()
        label_turtle.goto(0, 0)
        label_turtle.write(f"Time's up! Score: {score}", align="center", font=("Arial", 24, "bold"))


t.onclick(update_score)

def my_task():
    t.goto(random.randint(-250, 250), random.randint(-250, 250))


label_turtle = turtle.Turtle()
label_turtle.hideturtle()
label_turtle.penup()
update_labels()


schedule.every(0.5).seconds.do(my_task)

schedule.every(1).seconds.do(countdown)

while True:
    schedule.run_pending()
    board.update()
    time.sleep(0.1)
