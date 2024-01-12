x=10
dirX=10


def setup():
    size(900,900)
    background(1)

def draw():
    fill(255,255,255)
    if mouseButton == LEFT:
        fill(242,12,227)
        ellipse(mouseX,mouseY,25,25)
    if mouseButton == RIGHT:
        fill(2,219,79)
        ellipse(mouseX,mouseY,50,50)
    if mouseButton == CENTER:
        background(1)
        
        
    
    
    
    
