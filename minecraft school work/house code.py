import mcpi.minecraft as minecraft # imports mcpi.minecraft and renames it as minecraft
import time # imports the time command
import random
mc = minecraft.Minecraft.create() # this connects the code to a minecraft world

time.sleep(1) # waits 1 second

mc.player.setPos(0,0,0) # sets the player position to 0,0,0

time.sleep(2) # waits 2 seconds

mc.setBlocks(-30,-5,-30,30,30,30,0) # cuts out an area to work in

def house(x,y,z): # defines the function house
    
    mc.setBlocks(x+1,y,z+1,x+5,y+6,z+7,5)
    mc.setBlocks(x+2,y+1,z+2,x+4,y+5,z+6,0)
    mc.setBlocks(x+3,y+1,z+1,x+3,y+2,z+2,0)
    mc.setBlocks(x+2,y+6,z+2,x+4,y+6,z+6,20)
    time.sleep(5)

house(20,0,20)
house(30,0,20)
house(40,0,20)




