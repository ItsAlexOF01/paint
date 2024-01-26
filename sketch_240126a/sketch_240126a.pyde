b=0


def setup():
    size(900,900)
    background(0,0,0)
    
    
    
def draw():
    background(b)
    text(b,300,200)
    
    
def mouseClicked():
    global x
    global b
    if mouseX > 20 and mouseX < 70 and mouseY > 30 and mouseY < 80:
        b = 255
    mouseButton == RIGHT:
        b=b+1
        
    
    
        
