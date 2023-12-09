#Made for Karel in CodeHS
"""
karel will make 3 ball towers on columns 2 and 4 and will end on top of second tower facing east
"""

#Karel will create ball tower
def ball_tower():
    turn_left()
    put_ball()
    move()
    put_ball()
    move()
    put_ball()

#Karel will move down ball tower
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

#Ball Tower 1
move()
ball_tower()
move_down()

#Moving to where ball tower 2 will be built
move()
move()

#Building Ball tower 2
ball_tower()
move()
turn_right()
