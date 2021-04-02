import random
import sys
import tkinter
import pygame #for vscode to be able to import pygame, even after using pip install pygame,i had to use 'py -3.9 -m pip install pygame'
#so that pygame build 2 can be installed. for python 3.9 is compatible with pygame 2
import math
from tkinter import messagebox
#from pygame.locals import *

class cube(object):
    rows=1
    w=0
    def __init__(self,start,dx=1,dy=0,color=(255,0,0)):
        self.pos=start
        self.dx=1
        self.dy=0
        self.color=color


    def draw(self,surface,eyes=False):
        dis=self.w//self.rows
        i=self.pos[0]
        j=self.pos[1]

        pygame.draw.rect(surface,self.color,(i*dis+1,j*dis+1,dis-2,dis-2))
        if eyes:
            centre=dis//2
            radius=3
            circleMiddle=(i+dis+centre-radius,j*dis+1)
            circleMiddle2=(i+dis+dis-radius*2,j*dis+8)
            pygame.draw.circle(surface,(0,0,0),circleMiddle,radius)
            pygame.draw.circle(surface,(0,0,0),circleMiddle2,radius)

    def move(self,dx,dy):
        self.dx=dx
        self.dy=dy
        self.pos(self.pos[0]+self.dx,self.pos[1]+ self.dy)


class snake(object):
    body=[]
    turns={}
    def __init__(self,color,pos):
        self.color=color
        self.head=cube(pos)
        self.body.append(self.head)
        self.dx=0
        self.dy=1
    
    def move(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

            keys=pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dx=-1
                    self.dy=0
                    self.turns[self.head.pos[:]]=[self.dx,self.dy]
                elif keys[pygame.K_RIGHT]:
                    self.dx=1
                    self.dy=0
                    self.turns[self.head.pos[:]]=[self.dx,self.dy]
                elif keys[pygame.K_UP]:
                    self.dx=0
                    self.dy=-1
                    self.turns[self.head.pos[:]]=[self.dx,self.dy]
                elif keys[pygame.K_DOWN]:
                    self.dx=0
                    self.dy=1
                    self.turns[self.head.pos[:]]=[self.dx,self.dy]
        for i,c in enumerate(self.body):
            p=c.pos[:]
            if p in self.turns:
                turn=self.turns[p]
                c.move(turn[0],turn[1])
                if i==len(self.body)-1:
                    self.turns.pop(p) #removes the turn at the end of the cubes
            else: #checking if we have reached the end of the screen
                if c.dx==-1 and c.pos[0] <=0: c.pos=(c.rows-1,c.pos[1])
                elif c.dx==1 and c.pos[0] >=c.rows-1: c.pos=(0,c.pos[1])
                elif c.dx==1 and c.pos[1] >=c.rows-1: c.pos=(c.pos[0],0)
                elif c.dx==-1 and c.pos[0] <=0: c.pos=(c.pos[0],c.rows-1)
                else:
                    c.move(c.dx,c.dy)

    def draw(self,surface):
        for i,c in enumerate(self.body):
            if i==0:
                c.draw(surface,True)
            else:
                c.draw(surface)
def drawGrid(w,rows,surface):
    sizeBtw= w//rows
    x=0
    y=0
    for i in range(rows):
        x=x+sizeBtw
        y=y+sizeBtw

        #draw the horizontal and vertical lines forming the grid
        pygame.draw.line(surface,(255,255,255),(x,0),(x,w))
        pygame.draw.line(surface,(255,255,255),(0,y),(w,y))


def redrawWindow(surface):
    surface.fill((0,0,0)) #fill the window color
    s.draw(surface) #this line draws the snake
    drawGrid(width,rows,surface)
    pygame.display.update()

def main():
    global rows,width,s
    width=500
    rows=20
    win=pygame.display.set_mode((width,width))
    #creating snake object
    s=snake((255,0,0),(10,10)) #the snake object takes in two arguments,color and position
    flag= True
    while flag:
        clock=pygame.time.Clock()
        pygame.time.delay(50) #delays clock tick by 50 milliseconds
        clock.tick(10) #for snake to move ten blocks per second
        redrawWindow(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() #This line will help to exit the pygame window when you click the close button
                #we can also use pygame.quit() which ends all modules(display,mixer,font ,etc) opened by pygame.init(). all
                #we can also use pygame.display.quit() which closes the display opened by pygame.display.init()
    
main()