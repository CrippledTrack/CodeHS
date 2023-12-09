#Made for Karel in CodeHS
def ball_tower():
    turn_left()
    put_ball()
    move()
    put_ball()
    move()
    put_ball()

def move_down():
    turn_left()
    turn_left()
    move()
    move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

move()
ball_tower()
move_down()
move()
move()
ball_tower()
move()
turn_right()
