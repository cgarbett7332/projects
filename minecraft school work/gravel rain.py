import mcpi.minecraft as minecraft # imports mcpi.minecraft and renames it minecraft
import time # imports the time command
import random
mc = minecraft.Minecraft.create() # connects to the minecraft world so the program can be run.

while True: # makes an infinite loop
    pos = mc.player.getPos() # gets the players position and names it pos
    x = int(pos.x)
    print x
    y = int(pos.y)
    print y
    z = int(pos.z)
    print z

    block=13 # this is the block ID of gravel

    x = random.randint(x-10,x+10)
    z = random.randint(z-10,z+10)
    mc.setBlock(x,y+50,z,block)
    time.sleep(0.2)
