from asyncio import events
import pygame_widgets
import pygame as pg
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame import *
import time 
#this code is a mess jesus
pg.init()
win = pg.display.set_mode((1000,800))
circles = []
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
txtbox.setText("hide")
filebox.setText("file")
savebox.setText("save")
openbox.setText("open")
#hides the sliders or shows them
def openfile(filename):
    file = open(f"{filename}.txt","r")
    circle =[]
    for i in file:
        a = i.split()
        b = list(map(float,a))     
        circle.append(b)
    return(circle)
def save(filename):
    file = open(f"{filename}.txt","a+")
    file.truncate(0)
    for i in circles:
        file.write(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} \n")
    file.close
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
#this function gets the values of all the sliders 
def colour():
    s = size.getValue()
    rvalue= red.getValue()
    gvalue=green.getValue()
    bvalue=blue.getValue()
    pg.draw.circle(win,(rvalue,gvalue,bvalue),(850,50),s)
    rgb.setText((rvalue,gvalue,bvalue))
    return(rvalue,gvalue,bvalue,s)
win.fill((255,255,255))
frame_cap = 1.0/60
time_1 = time.perf_counter()
unprocessed = 0
while True:
    can_render = False
    time_2 = time.perf_counter()
    passed = time_2 - time_1
    unprocessed += passed
    time_1 = time_2
    pg.draw.rect(win,(255,255,255),(0,0,1000,140))
    events = pg.event.get()
    mx,my = pg.mouse.get_pos()
    # txtset()
    r,g,b,s=colour()
    if pg.mouse.get_pressed()[0] and my>140 and [mx,my,s,r,g,b] not in circles:
        pg.draw.circle(win,(r,g,b),(mx,my),s)
        circles.append([mx,my,s,r,g,b])
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
            hidebutton = Rect(205,0,50,30)
            filebutton = Rect(0,0,50,30)
            openb = Rect(0,60,50,30)
            saveb = Rect(0,30,50,30)

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
        # put everything inside here

        pg.display.update()
