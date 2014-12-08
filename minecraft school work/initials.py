import mcpi.minecraft as minecraft
import time
import random
mc = minecraft.Minecraft.create()

mc.setBlocks(-30,-5,-30,30,30,30,0)

red=14

def C(x,y,z):
    for height in(1,2,3,4,5):
        mc.setBlock(x,y+height,z,35,14)
    for location in(1,2,3):
        mc.setBlock(x+location,y,z,35,14)
    for location in(1,2,3):
        mc.setBlock(x+location,y+6,z,35,14)
    for height in(1,5):
        mc.setBlock(x+4,y+height,z,35,14)

def G(x,y,z):        
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











