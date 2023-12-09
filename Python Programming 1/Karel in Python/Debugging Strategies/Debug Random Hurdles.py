#Made for Karel in CodeHS
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(13):
    if front_is_blocked():
        jump_hurdle()
    else:
        front_is_clear()
        move()
