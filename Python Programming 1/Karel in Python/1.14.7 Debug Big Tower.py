#Made for Karel in CodeHS
def turn_north():
    while not_facing_north():
        turn_left()

def build_tower():
    while front_is_clear():
        put_ball()
        move()

turn_north()
build_tower()
put_ball()
