#Made for Karel in CodeHS
def build_tower():
    turn_left()
    put_ball()
    move()
    put_ball()
    move()
    put_ball()
    turn_around()
    move()
    move()
    turn_left()

build_tower()

if front_is_clear():
    move()
    move()
    build_tower()
    turn_right()
    turn_left()

if front_is_clear():
    move()
if front_is_clear():
    move()
    build_tower()

if front_is_clear():
    move()
    move()
    build_tower()
    move()
