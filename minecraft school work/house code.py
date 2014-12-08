import mcpi.minecraft as minecraft
import time
import random
mc = minecraft.Minecraft.create()

time.sleep(1)

mc.player.setPos(0,0,0)

time.sleep(2)

mc.setBlocks(-30,-5,-30,30,30,30,0)

def house(x,y,z):
    
    mc.setBlocks(x+1,y,z+1,x+5,y+6,z+7,5)
    mc.setBlocks(x+2,y+1,z+2,x+4,y+5,z+6,0)
    mc.setBlocks(x+3,y+1,z+1,x+3,y+2,z+2,0)

    mc.setBlocks(x+2,y+6,z+2,x+4,y+6,z+6,20)

    time.sleep(5)


house(20,0,20)
house(30,0,20)
house(40,0,20)




