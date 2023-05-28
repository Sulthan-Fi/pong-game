# Simple Pong Game 
# By Sulthan 
# email:[sulthanishq@gmail.com] LinkedIn:[linkedin.com/in/sulthan-ishq]

import turtle 

# Window setting
wn = turtle.Screen()
wn.title("Pong by @Sulthan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Menu options
options = ["START GAME", "About", "Quit"]
current_option = 0
confirm_key = False
escape_key = False

# Create a pen for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 100)

# Check if the game in menu or not
in_menu = True
in_game = False
in_setting = False
in_about = False 

# Function to select a menu
def confirm_action():
    global confirm_key
    confirm_key = True

def escape_action():
    global escape_key
    escape_key = True

# Function to move up in the menu
def move_up():
    global current_option
    if current_option > 0:
        current_option -= 1
    update_menu()

# Function to move down in the menu
def move_down():
    global current_option
    if current_option < len(options) - 1:
        current_option += 1
    update_menu()

# Function to update the menu display
def update_menu():
    pen.clear()
    pen.setheading(270)
    pen.penup()
    pen.goto(0, 100)
    pen.pendown()
    pen.write("Pong", align="center", font=("Courier", 48, "normal"))

    pen.penup()
    pen.goto(0, 50)
    pen.pendown()

    for i, option in enumerate(options):
        if i == current_option:
            pen.write(f"> {option} <", align="center", font=("Courier", 24, "normal"))
        else:
            pen.write(option, align="center", font=("Courier", 24, "normal"))
        pen.penup()
        pen.forward(50)
        pen.pendown()

# Function to clear screen
def clear_screen():
    pen.clear()

# Function to start the game
def start_game():
    # clear the screen and start the game 
    clear_screen()
    global in_menu, in_game
    in_menu = False
    in_game = True
    
    # Score
    score_a = 0
    score_b = 0 

    # Paddle A asset
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B asset
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball asset
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.12
    ball.dy = -0.12

    # Pen drawing scoreboard
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

    # Player control function
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)
    
    # Player key binding 
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")
    wn.onkeypress(confirm_action, "Return") # Add event listener


    # Main game loop 
    while in_game:
        wn.update()

        # Move the ball 
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 285:
            ball.sety(285)
            ball.dy *= -1
        
        if ball.ycor() < -285:
            ball.sety(-285)
            ball.dy *= -1
        
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 
        
        # Paddle and ball collision
        if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1

# Function to update about display
def update_about():
    global in_menu, in_about
    in_menu = False
    in_about = True

    pen.clear()
    pen.penup()
    pen.goto(0, 100)
    pen.pendown()
    pen.write("About", align="center", font=("Courier", 48, "normal"))

    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.write("Name: Sulthan", align="center", font=("Courier", 24, "normal"))

    pen.penup()
    pen.goto(0, -50)
    pen.pendown()
    pen.write("Email: sulthanishq@gmail.com", align="center", font=("Courier", 24, "normal"))

    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.write("linkedin.com/in/sulthan-ishq", align="center", font=("Courier", 24, "normal"))

# Initial menu display
if in_menu:
    update_menu()

# Keyboard binding
wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(confirm_action, "Return")
wn.onkeypress(escape_action, "Escape")

# Main program loop
while True:
    wn.update()

    # Flow logic
    if in_menu: 
        if confirm_key:
            selected_option = options[current_option]

            # check if player select start game, about, or quit
            if selected_option == "START GAME":
                start_game()

            if selected_option == "About":
                update_about()

            if selected_option == "Quit":
                exit()
