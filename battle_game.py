# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 19:28:32 2015

@author: George

Little script to mess around with OOP in python. A simulated battle between
a hero and villain.
"""
import random
import time

#base class needs to inherit from object so that super in subclasses works
#correctly. Super can only be used in new style classes, that is classes
#where the root class inherits from object.

# Fighter base class
class Fighter(object):  
    
    def __init__(self,name='fighter'):
        self.health=100
        self.name=name
        
    def do_move(self):
        print 'fighter strike'
    
    def is_alive(self):
        if self.health>0:
            return True


         
class Hero(Fighter):
    
    '''
    Hero inherits from fighter and overrides do_move.
    '''    
    # The hero name is passed through super to the base class constructor.   
    def __init__(self):
        super(Hero,self).__init__('Hero')        
        print 'Hero created'
        
    def do_move(self):
        print 'Hero lance'

 

class Villain(Fighter):
    '''
    Villain inherits from fighter and overrides do_move.
    '''    
    # The Villain name is passed through super to the base class constructor.
    def __init__(self):
        super(Villain,self).__init__('Villain')        
        print 'Villain created'
        
    def do_move(self):
        print 'Sneaky slap'

    
class BattleField(object):
    '''
    The stage for epic battles.
    '''
    
    # Pass in two fighters.    
    def __init__(self,fighter1,fighter2):
        self.fighter1=fighter1
        self.fighter2=fighter2
    
    # Method to find winner and print result. 
    def announce_winner(self):
        if self.fighter1.health>0:
            print self.fighter1.name+' is victorious'
        elif self.fighter2.health>0:
            print self.fighter2.name+' is victorious'
    
    # A method to control the fight. A random number between 0 and 1 is
    # used to determine who does damage.
    def let_the_battle_commence(self):
        fighters = [self.fighter1,self.fighter2]        
        
        while (fighters[0].is_alive() and fighters[1].is_alive()):
            fighter_num = random.randint(0,1)            
            fighters[fighter_num].do_move()
            fighters[(fighter_num+1)%2].health-=10
            # Can add delay to increase the suspense.
            #time.sleep(1)
        self.announce_winner()
        
if __name__=='__main__':
    
    BattleField(Hero(),Villain()).let_the_battle_commence()
        
                
