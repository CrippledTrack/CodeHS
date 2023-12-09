#Made for Karel in CodeHS
def safemove():
    if front_is_clear():
        move()

def checkerpaint():
    for i in range(4):
        paint(color["black"])
        safemove()
        paint(color["red"])
        safemove()

for i in range(4):
    checkerpaint()    
    turn_left()
    safemove()
    turn_left()
    checkerpaint()
    turn_right()
    safemove()
    turn_right()
    
turn_right()
for i in range(7):
    move()
turn_left()
