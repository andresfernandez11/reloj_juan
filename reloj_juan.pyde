s = 0
a = 0
z = 0
def setup ():
    size (300, 300)
def draw():
    background(0)
    global s
    global a
    global z
    square(s, 2, 55)
    if s > height:
       s = 0
    else:
       s = map(second(), 0, 59, 0, height)
    circle(a, 130, 58)
    if a > height:
       a = 0
    else:
       a = map(minute(), 0, 59, 0, height)
    square(z, 200, 80)
    if z > height:
       z = 0
    else:
       z = map(hour(), 0, 59, 0, height)
