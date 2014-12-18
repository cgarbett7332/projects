import mcpi.minecraft as minecraft # imports mcpi. minecraft and renames it minecraft
import time # imports time commands e.g. time.sleep(1).
import random
mc = minecraft.Minecraft.create() # this connects to a minecrfat world that is open so the program can be run.

mc.setBlocks(-30,-5,-30,30,30,30,0) # cuts out an area to work in.

for b in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16):
    mc.postToChat(b)
    mc.setBlock(0,b,0,35,b)
    time.sleep(2)
        
    
