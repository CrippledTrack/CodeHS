#Made for Karel in CodeHS
while not_facing_north():
    turn_left()

while no_balls_present():
    put_ball()
    if front_is_clear():
        move()
