#Made for Karel in CodeHS
def put_balls_in_row():
    move()
    put_ball()
    move()
    put_ball()
    move()
    put_ball()
    move()
    put_ball()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def make_diagonal():
    turn_right()
    move()
    turn_right()
    move()
    put_ball()
    
    turn_left()
    move()
    turn_right()
    move()
    put_ball()

    turn_left()
    move()
    turn_right()
    move()

put_balls_in_row()
make_diagonal()
move()
turn_around()
put_balls_in_row()
