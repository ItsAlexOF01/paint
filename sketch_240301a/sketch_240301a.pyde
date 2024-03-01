x=10
dirX=10


def setup():
    size(900,900)
    background(1)

def draw():
    fill(255,255,255)
    if mouseButton == LEFT:
        textSize(50)
        text(u"BU!!!",500,250)
        fill(255,102,0)
        ellipse(450,450,300,300)
        fill(255,255,255)
        ellipse(500,415,100,100)
        fill(0,0,0)
        ellipse(500,415,30,30)
        fill(255,255,255)
        ellipse(400,415,100,100)
        fill(0,0,0)
        ellipse(400,415,30,30)
        fill(234,149,195)
        rect(415,490,100,10)
    if mouseButton == RIGHT:
        fill(2,219,79)
        ellipse(mouseX,mouseY,50,50)
    if mouseButton == CENTER:
        background(1)
