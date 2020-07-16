import turtle
import random
import math
import os

scrn = turtle.Screen()
scrn.bgcolor("black")
scrn.title("Space Scrapper")
scrn.bgpic("space_station_defense_game_background.gif")
scrn.setup(800, 800)
scrn.tracer(0)

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align="left", font=("Arial", 14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()

    def play_sound(self, filename):
        os.system("afplay {}&".format(filename))

class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.shapesize(0.5, 1.0, None)
        self.color("teal")
        self.speed = 0
        self.lives = 3

    def rotate_left(self):
        self.lt(30)

    def rotate_right(self):
        self.rt(30)

    def move(self):
        self.fd(self.speed)

        if self.xcor() > 290 or self.xcor() < -290:
            self.lt(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.lt(60)

    def accelerate(self):
        self.speed += 1

    def deccelerate(self):
        self.speed -= 1

colors = ["red", "white", "blue", "green", "gold"]

class Scrap(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color(random.choice(colors))
        self.shape("turtle")
        self.speed = 3
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def hyperspace_jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))
        self.color(random.choice(colors))

    def move(self):
        self.fd(self.speed)

        if self.xcor() > 290 or self.xcor() < -290:
            self.lt(60)
            game.play_sound("bounce.wav")
        if self.ycor() > 290 or self.ycor() < -290:
            self.lt(60)
            game.play_sound("bounce.wav")

class Pirate(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color(random.choice(colors))
        self.shape("classic")
        self.speed = 3
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(self.speed)

        if self.xcor() > 290 or self.xcor() < -290:
            self.lt(60)
            game.play_sound("bounce.wav")
        if self.ycor() > 290 or self.ycor() < -290:
            self.lt(60)
            game.play_sound("bounce.wav")

def isCollision(t1, t2):
    a = t1.xcor()-t2.xcor()
    b = t1.ycor()-t2.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))

    if distance < 20:
        return True
    else:
        return False

running = True

def quit():
    global running
    running = False

player = Player()
border = Border()
game = Game()

border.draw_border()

scraps = []
for count in range(6):
    scraps.append(Scrap())

pirates = []
for count in range(6):
    pirates.append(Pirate())

scrn.listen()
scrn.onkeypress(player.rotate_left, "Left")
scrn.onkeypress(player.rotate_right, "Right")
scrn.onkeypress(player.accelerate, "Up")
scrn.onkeypress(player.deccelerate, "Down")
scrn.onkeypress(quit, "q")

while running:
    scrn.update()
    player.move()
    for scrap in scraps:
        scrap.move()

        if isCollision(player, scrap):
            scrap.hyperspace_jump()
            game.change_score(100)
            game.play_sound("power.wav")

    for pirate in pirates:
        pirate.move()

        if isCollision(player, pirate):
            player.goto(0, 0)
            player.speed = 0
            game.change_score(-50)
            player.lives -= 1
            game.play_sound("explosion.mp3")
            print("Your ship was attacked by pirates! -1 life")

    if player.lives == 0:
        print("you suck nuub, you died")
        break