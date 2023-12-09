#Made for Karel in CodeHS
def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(5):
    move()
    move()
    jump_hurdle()
