import mcpi.minecraft as minecraft
import time
import random
mc = minecraft.Minecraft.create()

mc.setBlocks(-30,-5,-30,30,30,30,0)

#loops through 0-16 and uses these for the y coordinates and colour
for b in range (14,0,-1):
    mc.postToChat(b)
    mc.setBlock(0,b,0,35,b)
    time.sleep(2)
        
    
