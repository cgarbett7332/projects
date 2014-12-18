import mcpi.minecraft as minecraft # imports mcpi.minecraft and renames it minecraft
import time # imports time commands e.g. time.sleep(1)
import random 
mc = minecraft.Minecraft.create() # this connects to a minecraft world so the program can be run on it.

mc.setBlocks(-30,-5,-30,30,30,30,0)

#loops through 0-16 and uses these for the y coordinates and colour
for b in range (14,0,-1):
    mc.postToChat(b)
    mc.setBlock(0,b,0,35,b)
    time.sleep(2)
        
    
