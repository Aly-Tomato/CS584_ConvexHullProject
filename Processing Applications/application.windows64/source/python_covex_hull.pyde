import Utils
import Jarvis
import Grahams

#global variables
master = []
click_count = 0
i = 1
convex_list = []
bChanged = False

    
def setup():
    """ initial setup of the screen """
    fullScreen()
    frameRate(3)
    background(255)

   
def mouseClicked():
    """ 
    Describes the actions when mouse is clicked by user.
    User will use this action to decide when to stop generating
    points and to start performing the convex hull algorithm on
    the set of points
    """
    global click_count
    if(len(master) < 3):
        print("ERROR: Must have at least 3 points")
        exit()
    if click_count == 0:
        do_test()
    click_count +=1
    
    
def do_test():
    global convex_list
    convex_list = Jarvis.do_Jarvis(master)
    delay(200)
    
def change_setup():
    global bChanged
    global click_count
    if(bChanged == False):
        background(0)
        frameRate(300)
        bChanged = True
        click_count +=1
        
    
def draw_convex_hull():
    """ Helper function to calculate the lines to draw next """
    global i
    global convex_list
    global click_count
    if i < len(convex_list):
        a = convex_list[i-1].x
        b = convex_list[i-1].y
        c = convex_list[i].x 
        d = convex_list[i].y 
        line(a,b,c,d)
        i += 1
    else:
        i = 1
        click_count += 1

        
def draw():
    """ Statements in this body will execute per frame """
    B = Utils.create_point()
    master.append(B)
    global i
    global click_count
    if(click_count == 0):
        #Still drawing random dots
        noStroke()
        fill(0)
        ellipse(B.x,B.y,15,15)
        myFont = createFont("Book Antiqua", 60)
        textFont(myFont)
        textAlign(CENTER, CENTER)
        text("Click Anywhere", width/2, height/2)
    elif(click_count == 1):
        #Ready to apply algo and draw lines
        stroke(0)
        draw_convex_hull()    
    elif(click_count == 2):
        change_setup()
    else:
        fill(random(255),random(255),255)
        textAlign(CENTER, CENTER)
        strokeWeight(10)
        stroke(random(255),random(255),255)
        draw_convex_hull()
        myFont = createFont("Courier", 60*i)
        textFont(myFont)
        textAlign(CENTER, CENTER)
        text("ESC", width/2, height/2)

        
        
        

        
