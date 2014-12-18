import mcpi.minecraft as minecraft # imports mcpi.minecraft and renames it minecraft
import time
mc = minecraft.Minecraft.create()

while True: # creates an infinite loop
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y-1
    z = pos.z

    block=41 # this makes is the block ID for gold.

    mc.setBlock(x,y,z,block) # this places gold underneath the player forever until the code it stopped
    time.sleep(0.2)
