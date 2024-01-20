x=10
dirX=10



def setup():
    size(900,900)
    
    
    
def draw():
    if mouseButton == RIGHT:
        global x
        global dirX
        background(1)
        fill(random(255),random (255), random (255))
        ellipse(x,100,50,50)
        x=x+dirX
        if x < 870:
            dirX=-10
            
    if mouseButton == LEFT:
        global x
        global dirX
        background(1)
        fill(random(255), random(255), random(255))
        ellipse(x,100,50,50)
        x=x+dirX
        if x > 10:
            dirX=+10
            

            
            

        
            


    
    
