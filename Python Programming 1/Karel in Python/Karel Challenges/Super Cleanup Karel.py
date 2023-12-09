#Made for Karel in CodeHS
def pickupmove():
    while front_is_clear():
        if balls_present():
            take_ball()
            move()
        else:
            move()
            
def safemove():
    if front_is_clear():
        move()
        
def left_turn():
    if balls_present():
        take_ball()
        turn_left()
        safemove()
        turn_left()
    else:
        turn_left()
        safemove()
        turn_left()
        
def right_turn():
    if balls_present():
        take_ball()
        turn_right()
        safemove()
        turn_right()
    else:
        turn_right()
        safemove()
        turn_right()

for i in range(15):
    pickupmove()
    left_turn()
    pickupmove()
    right_turn()
