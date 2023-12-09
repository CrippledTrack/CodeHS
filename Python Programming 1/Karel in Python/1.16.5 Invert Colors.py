#Made for Karel in CodeHS
def paint_red():
    paint(color["red"])

def paint_blue():
    paint(color["blue"])
    
def safemove():
    if front_is_clear():
        move()
    
for i in range(10):
    if color_is(color["red"]):
        paint_blue()
        safemove()
    else:
        if color_is(color["blue"]):
            paint_red()
            safemove()
