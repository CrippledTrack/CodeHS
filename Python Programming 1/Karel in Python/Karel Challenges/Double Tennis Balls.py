#Made for Karel in CodeHS
def face():
    turn_around()
    move()
    turn_around()
move()
for i in range(7):
    take_ball()
if no_balls_present():
    for i in range(14):
        put_ball()
    face()
    
if balls_present():
    for i in range(28):
        put_ball()
    face()
