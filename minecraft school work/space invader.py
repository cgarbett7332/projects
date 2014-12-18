import mcpi.minecraft as minecraft   #imports mcpi.minecraft but names it as minecraft.
import time   #imports time commands e.g. time.sleep(1).
import random   #imports the random commands but you don't need it for this code.
mc = minecraft.Minecraft.create() #connects to a minecraft world that is open so the code can run.

mc.setBlocks(-30,-5,-30,30,30,30,0) #cuts out a big area to work in.
time.sleep(3)    #sleeps for 3 seconds.

#lists all the colour wools as numbers(their ID's so the program can use it to change the colour of the space invader).
orange=1
magenta=2
light_blue=3
yellow=4
lime=5
pink=6
gray=7
light_gray=8
cyan=9
purple=10
blue=11
brown=12
green=13
red=14
black=15

def space_invader(colour):    #defines space_invader(colour), and uses for loops to place blocks that make a space invader and it does it in rows
    for location in(4,5,7,8):
        mc.setBlock(location,0,0,35,colour) #sets blocks at that location (x=location,y=0,z=0) the 35 represents the block wool, because wool's ID is 35. 
    for location in(1,3,9,11):
        mc.setBlock(location,1,0,35,colour) #sets blocks at that location (x=location,y=1,z=0) the 35 represents the block wool, because wool's ID is 35.
    for location in(1,3,4,5,6,7,8,9,11):
        mc.setBlock(location,2,0,35,colour) #sets blocks at that location (x=location,y=2,z=0) the 35 represents the block wool, because wool's ID is 35.
    for location in(1,2,3,4,5,6,7,8,9,10,11):
        mc.setBlock(location,3,0,35,colour) #sets blocks at that location (x=location,y=3,z=0) the 35 represents the block wool, because wool's ID is 35.
    for location in(2,3,5,6,7,9,10):
        mc.setBlock(location,4,0,35,colour) #sets blocks at that location (x=location,y=4,z=0) the 35 represents the block wool, because wool's ID is 35.
    for location in(3,4,5,6,7,8,9):
        mc.setBlock(location,5,0,35,colour) #sets blocks at that location (x=location,y=5,z=0) the 35 represents the block wool, because wool's ID is 35.
    for location in(4,8):
        mc.setBlock(location,6,0,35,colour) #sets blocks at that location (x=location,y=6,z=0) the 35 represents the block wool, because wool's ID is 35.
    for location in(3,9):
        mc.setBlock(location,7,0,35,colour) #sets blocks at that location (x=location,y=7,z=0) the 35 represents the block wool, because wool's ID is 35.
    time.sleep(0.20)   #sleeps for 0.20 seconds and then using the infinite loop underneath will repeat changing colour each time.

while True:  #creates an infinite loop
    for colour in(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15): # the id for each of the wool, this is what changes its colour.
        space_invader(colour)   #makes the space invader change colour using the colour list at the top in order.
  


    























    




