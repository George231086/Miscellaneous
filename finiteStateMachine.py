'''

Unfinished. I've modified the finite state machine implementation found in the youtube video 
https://www.youtube.com/watch?v=E45v2dD3IQU&index=8&list=PL82YdDfxhWsC-3kdTKK2_mwbNdBfVvb_M
to create an object wanderer which has the states moving forward, backwards, left or right. Using pygame I've 
hooked this up to a simple frame. The wanderer is represented by a rectangle and just aimlessly moves around the window.
I'll add more states such as changing colour as I continue working on it. My aim is to the fill the frame with
moving objects and add some behaviour for when they collide.

'''

import pygame, sys
from pygame.locals import *
from random import randint
from time import clock

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

FPS=30

class Transition(object):
    
    def __init__(self,toState):
        self.toState=toState
        
    def Execute(self):
        print 'Transitioning'
        
        
class State(object):
    
    def __init__(self,FSM):
        self.FSM=FSM
        self.timer=0
        self.startTime=0
        
    def Enter(self):
        self.timer=randint(0,5)
        self.startTime=int(clock())
    
    def Execute(self):
        pass
    
    def Exit(self):
        pass
    
class MovingLeft(State):
    
    def __init__(self,FSM):
        super(MovingLeft,self).__init__(FSM)
    
    def Enter(self):
        print "starting to move left"
        super(MovingLeft,self).Enter()
    
    def Execute(self):
        print "moving left"
        self.FSM.alterCoords(-10,0)
        self.FSM.signalChange()
        if (self.startTime+self.timer<=clock()):
            trans = ['moveUp','moveDown','moveRight'][randint(0,2)]
            self.FSM.ToTransition(trans)    
                
    def Exit(self):
        print 'finished moving left'    
        
class MovingRight(State):
    
    def __init__(self,FSM):
        super(MovingRight,self).__init__(FSM)
    
    def Enter(self):
        print "starting to move right"
        super(MovingRight,self).Enter()
    
    def Execute(self):
        print "moving Right"
        self.FSM.alterCoords(10,0)
        self.FSM.signalChange()
        if (self.startTime+self.timer<=clock()):
            trans = ['moveUp','moveDown','moveLeft'][randint(0,2)]
            self.FSM.ToTransition(trans)    
            
    def Exit(self):
        print 'finished moving right'        

class MovingUp(State):
    
    def __init__(self,FSM):
        super(MovingUp,self).__init__(FSM)
        
    def Enter(self):
        print "starting to move up"
        super(MovingUp,self).Enter()
    
    def Execute(self):
        print "moving up"
        self.FSM.alterCoords(0,-10)
        self.FSM.signalChange()
        if (self.startTime+self.timer<=clock()):
            trans = ['moveLeft','moveDown','moveRight'][randint(0,2)]
            self.FSM.ToTransition(trans)    
            
    def Exit(self):
        print 'finished moving up'    
        
class MovingDown(State):
    def __init__(self,FSM):
        super(MovingDown,self).__init__(FSM)
        
    def Enter(self):
        print "starting to move down"
        super(MovingDown,self).Enter()
    
    def Execute(self):
        print "moving down"
        self.FSM.alterCoords(0,10)
        self.FSM.signalChange()
        if (self.startTime+self.timer<=clock()):
            trans = ['moveUp','moveLeft','moveRight'][randint(0,2)]
            self.FSM.ToTransition(trans)    
            
    def Exit(self):
        print 'finished moving down'        
        
class FSM(object):
    
    def __init__(self,Char,canvasObj,coords):
        self.char=Char
        self.states={}
        self.transitions={}
        self.curState=None
        self.prevState=None
        self.trans=None
        self.canvasObj=canvasObj
        self.coords={'x':coords[0],'y':coords[1]}
        self.canvasObj.objectCoords.append(self.coords)

        pygame.init()

    def AddState(self,stateName,state):
        self.states[stateName]=state

    def AddTransition(self,transName,transition):
        self.transitions[transName]=transition

    def setState(self,stateName):
        self.prevState=self.curState
        self.curState=self.states[stateName]
    
    def alterCoords(self,x,y):
    	width,height = self.canvasObj.canvas.get_size()
        print self.coords['x'], self.coords['y'],width,height
        if (0 <= (self.coords['x']+x) and (self.coords['x']+x+20) <= width):
            self.coords['x']+=x
    	if (0 <= (self.coords['y']+y) and (self.coords['y']+y+20) <= height):
            self.coords['y']+=y
    
    def signalChange(self):
        self.canvasObj.drawObjects()
    
    def ToTransition(self,toTrans):
        self.trans=self.transitions[toTrans]
        
    def Execute(self):
        if (self.trans):
            self.curState.Exit()
            self.trans.Execute()
            self.setState(self.trans.toState)
            self.curState.Enter()
            self.trans=None
        self.curState.Execute()
        self.canvasObj.Update()

Char=type("Char",(object,),{})

class CanvasObject(object):

    def __init__(self):
        pygame.init()
        self.canvas=pygame.display.set_mode((500,400),0,32)
        pygame.display.set_caption('Wanderers')
        self.fpsClock=pygame.time.Clock()
        self.canvas.fill(WHITE)
        self.objectCoords=[]
    
    def drawObjects(self):
        self.canvas.fill(WHITE)
        for coords in self.objectCoords:
            pygame.draw.rect(self.canvas,RED,(coords['x'],coords['y'],20,20))
    
    def Update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
		self.drawObjects()
        pygame.display.update()
        self.fpsClock.tick(FPS)
    

class Wanderer(Char):
    
    def __init__(self,canvasObj,coords)    :
        self.FSM=FSM(self,canvasObj,coords)
        
        self.FSM.AddState("MovingLeft",MovingLeft(self.FSM))
        self.FSM.AddState("MovingRight",MovingRight(self.FSM))
        self.FSM.AddState("MovingUp",MovingUp(self.FSM))
        self.FSM.AddState("MovingDown",MovingDown(self.FSM))

        self.FSM.AddTransition("moveLeft",Transition("MovingLeft"))
        self.FSM.AddTransition("moveRight",Transition("MovingRight"))
        self.FSM.AddTransition("moveUp",Transition("MovingUp"))
        self.FSM.AddTransition("moveDown",Transition("MovingDown"))

        self.FSM.setState("MovingLeft")

    def Execute(self):
        self.FSM.Execute()



if __name__=='__main__':
    c=CanvasObject()
    width,height = c.canvas.get_size()	
    
    wanderers=[Wanderer(c,(randint(0,48)*10,randint(0,38)*10)) for i in range(10)]

    while True:
        startTime=clock()
        timeInterval=1
        while(startTime+timeInterval>clock()):
            pass
        for wanderer in wanderers:
            wanderer.Execute()
