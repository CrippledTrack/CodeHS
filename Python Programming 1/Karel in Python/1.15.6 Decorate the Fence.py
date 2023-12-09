#Made for Karel in CodeHS
for i in range(5):
    move()
    
turn_left()
for i in range(10):
    if right_is_blocked():
        put_ball()
    if front_is_clear():
        move()
