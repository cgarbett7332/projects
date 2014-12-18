import mcpi.minecraft as minecraft # imports mcpi.minecraft and renames it as minecraft
import time # imports the time commands
import random
mc = minecraft.Minecraft.create() # this helps connect the code to the minecraft world for it to work

mc.setBlocks(-30,-5,-30,30,30,30,0) # this cuts out an area to work in

red=14 # the red wool block

def C(x,y,z): # this defines the function C so it makes a letter c in red on minecraft
    for height in(1,2,3,4,5):
        mc.setBlock(x,y+height,z,35,14)
    for location in(1,2,3):
        mc.setBlock(x+location,y,z,35,14)
    for location in(1,2,3):
        mc.setBlock(x+location,y+6,z,35,14)
    for height in(1,5):
        mc.setBlock(x+4,y+height,z,35,14)

def G(x,y,z): # this defines the function G so it makes a letter g in red on minecraft      
    for height in(1,2,3,4,5):
        mc.setBlock(x+6,y+height,z,35,14)
    for location in(1,2,3):
        mc.setBlock(x+location+6,y+6,z,35,14)
    for location in(1,2,3):
        mc.setBlock(x+location+6,y,z,35,14)
    mc.setBlocks(x+9,y+2,z,x+10,y+2,z+0,35,14)
    for height in(1,5):
        mc.setBlock(x+10,y+height,z,35,14)

C(20,0,20)
C(30,0,20)
G(20,20,20)
G(30,20,20)











