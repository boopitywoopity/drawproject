#python -m auto_py_to_exe
from asyncio import events
import pygame_widgets
import pygame as pg
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame import *
import time 
from math import sqrt

#this code is a mess jesus
pg.init()
win = pg.display.set_mode((1540,750))
pg.display.set_caption("boopybrush")
circles = []
#the next lines make me want to kill myself and is convoluted as fuck
red = Slider(win,100,40,600,10, min=0,max =255,step=1,colour=(255,0,0))
green = Slider(win,100,60,600,10,min=0,max=255,step=1,colour=(0,255,0))
blue = Slider(win,100,80,600,10,min=0,max=255,step=1,colour=(0,0,255))
size = Slider(win,100,100,400,10,min=5,max=50,step=0.125)
rgb = TextBox(win,850,120,150,50,fontSize=30)
txtbox =TextBox(win,205,00,50,30,fontSize=20)
filebox = TextBox(win,0,0,50,30,fontSize=20)
savebox = TextBox(win,0,30,50,30,fontSize=20)
openbox = TextBox(win,0,60,50,30,fontSize=20)
txtboxfilename = TextBox(win,50,30,100,30,fontSize=20)
filebox.disable()
savebox.disable()
openbox.disable()
txtbox.disable()
txtbox.setText("slider")
filebox.setText("file")
savebox.setText("save")
openbox.setText("open")










#this function gets the values of all the sliders 






win.fill((255,255,255))
frame_cap = 1.0/60
time_1 = time.perf_counter()
unprocessed = 0
#white
r1 = 255
g1 = 255
b1 = 255
#blue
r2 =0
g2 = 0
b2 =255
#red
r3 =255
g3 = 0
b3 =0
#green
r4 =0
g4 = 255
b4 =0
#black
r5 =0
g5 = 0
b5 =0


mode = "draw"
#yeah I'm noting these down cus I wont fucking remember what any of these rectangles do lol
erasemode = Rect(1405,20,40,40)
drawmode = Rect(1480, 20,40,40)
hot1 = Rect(905,10,20,20)
hot2 = Rect(1000,10,20,20)
hot3 = Rect(1100,10,20,20)
hot4 = Rect(1200,10,20,20)
hot5 = Rect(1300,10,20,20)
#button to togle on eraser
pg.draw.rect(win,(232,160,152),erasemode)
#button to toggle on pen
pg.draw.rect(win,(0,0,0),drawmode)
#puts a black background on the first hotkey cus you cant see it otherwise... might be smarter to change the default hotkey to another colour than white...
pg.draw.rect(win,(0,0,0),(900,5,30,30))
#first hotkey
pg.draw.rect(win,(r1,g1,b1),hot1)
#second hotkey
pg.draw.rect(win,(r2,g2,b2),hot2)
#third hotkey
pg.draw.rect(win,(r3,g3,b3),hot3)
#fourth hotkey
pg.draw.rect(win,(r4,g4,b4),hot4)
#fifth hotkey
pg.draw.rect(win,(r5,g5,b5),hot5)
hidebutton = Rect(205,0,50,30)
filebutton = Rect(0,0,50,30)
openb = Rect(0,60,50,30)
saveb = Rect(0,30,50,30)

#hides the sliders or shows them
def openfile(filename):
    #file = open(f"C:\\Users\\antoi\\OneDrive\\Bureau\\Programming\\fun\\pygame\\drawfilefolder\\{filename}.txt","r")
    file = open(f"{filename}.txt","r")
    circle =[]
    for i in file:
        a = i.split()
        b = list(map(float,a))     
        circle.append(b)
    file.close()
    return(circle)



def save(filename):
    #file = open(f"C:\\Users\\antoi\\OneDrive\\Bureau\\Programming\\fun\\pygame\\drawfilefolder\\{filename}.txt","a+")
    file = open(f"{filename}.txt","a+")
    file.truncate(0)
    for i in circles:
        file.write(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} \n")
    file.close


#the eraser is janky as fuck and barely works
#needs to be fixed...
def erase():
    
    for circle in circles:
        if mx < circle[0]:
            distance = sqrt((circle[0]-mx)**2+(circle[1]-my)**2)
            print(distance)
        if mx == circle[0]:
            distance = s+circle[2]
        if mx > circle[0]:
            distance = sqrt((mx-circle[0])**2+(my-circle[1])**2)
        if distance <= circle[2]:
            circles.remove(circle)
    pg.draw.rect(win,(255,255,255),(0,140,1540,610))
    for i in circles:
        pg.draw.circle(win,(i[3],i[4],i[5]),(i[0],i[1]),i[2])
#this is aids but I'm too lazy to fix it...
def showhide(): 
    if showcol == False:
        red.hide()
        blue.hide()
        green.hide()
        size.hide()
    else:
        red.show()
        blue.show()
        green.show()
        size.show()
    if showsavebutton==False:
        savebox.hide()
        openbox.hide()
        txtboxfilename.hide()
    if showsavebutton ==True:
        savebox.show()
        openbox.show()
        txtboxfilename.show()
showcol = True
showsavebutton = False


def colour():
    s = size.getValue()
    rvalue= red.getValue()
    gvalue=green.getValue()
    bvalue=blue.getValue()
    pg.draw.circle(win,(rvalue,gvalue,bvalue),(850,50),s)
    rgb.setText((rvalue,gvalue,bvalue))
    return(rvalue,gvalue,bvalue,s)


while True:
    can_render = False
    time_2 = time.perf_counter()
    passed = time_2 - time_1
    unprocessed += passed
    time_1 = time_2
    events = pg.event.get()
    mx,my = pg.mouse.get_pos()
    pg.draw.rect(win,(255,255,255),(0,0,900,140))



    # txtset()
    r,g,b,s=colour()
    k = pg.key.get_pressed()
    if pg.mouse.get_pressed()[0] and my>140 and [mx,my,s,r,g,b] not in circles:
        if mode =="draw":
            if k[pg.K_z]:
                circles.append([mx,my,s,r1,g1,b1])
                pg.draw.circle(win,(r1,g1,b1),(mx,my),s)
            elif k[pg.K_x]:
                circles.append([mx,my,s,r2,g2,b2])
                pg.draw.circle(win,(r2,g2,b2),(mx,my),s)
            elif k[pg.K_c]:
                circles.append([mx,my,s,r3,g3,b3])
                pg.draw.circle(win,(r3,g3,b3),(mx,my),s)
            elif k[pg.K_v]:
                circles.append([mx,my,s,r4,g4,b4])
                pg.draw.circle(win,(r4,g4,b4),(mx,my),s)
            elif k[pg.K_b]:
                circles.append([mx,my,s,r5,g5,b5])
                pg.draw.circle(win,(r5,g5,b5),(mx,my),s)
            else:
                pg.draw.circle(win,(r,g,b),(mx,my),s)
                circles.append([mx,my,s,r,g,b])
        if mode =="erase":
            erase()
            continue




    for event in events:
        if event.type == pg.QUIT:
            quit()
            break
        
        if event.type== pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                try:
                    circles.pop(-1)
                except IndexError:
                    continue




        if event.type== pg.MOUSEBUTTONUP:

            #sets an invisible click to use to check collisions
            click = Rect(mx,my,1,1)
            if pg.Rect.colliderect(click,drawmode):
                mode = "draw"
            if pg.Rect.colliderect(click,erasemode):
                mode = "erase"
            if pg.Rect.colliderect(click,hot1):
                r1= r
                g1 =g 
                b1 =b
                pg.draw.rect(win,(r1,g1,b1),hot1)
                break
            if pg.Rect.colliderect(click,hot2):
                r2=r
                g2=g
                b2=b
                pg.draw.rect(win,(r2,g2,b2),hot2)
                break
            if pg.Rect.colliderect(click,hot3):
                r3=r
                g3=g
                b3=b
                pg.draw.rect(win,(r3,g3,b3),hot3)
                break
            if pg.Rect.colliderect(click,hot4):
                r4=r
                g4=g
                b4=b
                pg.draw.rect(win,(r4,g4,b4),hot4)
                break
            if pg.Rect.colliderect(click,hot5):
                r5=r
                g5=g
                b5=b
                pg.draw.rect(win,(r5,g5,b5),hot5)
                break
                
            


            #this is to hide the sliders and shit 
            if pg.Rect.colliderect(click,hidebutton):  
                showsavebutton=False
                if showcol == True:
                    showcol = False
                    break
                if showcol ==False:
                    showcol=True
                    break

            #this is for the drop down menu for the open and save file menu
            if pg.Rect.colliderect(click,filebutton):
                if showsavebutton==False:
                    showcol = False
                    showsavebutton = True
                    break
                if showsavebutton==True:
                    showsavebutton=False
                    break
            if pg.Rect.colliderect(click,saveb) and showsavebutton == True:
                save(txtboxfilename.getText())
            if pg.Rect.colliderect(click,openb) and showsavebutton == True:
                circles =openfile(txtboxfilename.getText())
                for i in circles:
                    pg.draw.circle(win,(i[3],i[4],i[5]),(i[0],i[1]),i[2])
                    

    showhide()
    




    pygame_widgets.update(events)
    while(unprocessed >= frame_cap):
        unprocessed -= frame_cap
        can_render = True

    if can_render:

        pg.display.update()
