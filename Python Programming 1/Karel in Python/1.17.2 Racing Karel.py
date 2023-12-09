#Made for Karel in CodeHS
def eight_ball():
    for i in range(8):
        put_ball()

def safe_move():
    while front_is_clear():
        move()

for i in range(4):
    eight_ball()
    safe_move()
    turn_left()
