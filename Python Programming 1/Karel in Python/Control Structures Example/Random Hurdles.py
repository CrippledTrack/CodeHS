#Made for Karel in CodeHS
for i in range(13):
    if front_is_clear():
        move()
    else:
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
