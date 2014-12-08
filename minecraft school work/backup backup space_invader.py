import mcpi.minecraft as minecraft   #imports mcpi.minecraft but names it as minecraft
import time   #imports time commands e.g. time.sleep(1)
import random   #imports the random commands but you don't need it for this code
mc = minecraft.Minecraft.create()   #connects to a minecraft world

mc.setBlocks(-30,-5,-30,30,30,30,0) #cuts out a big area to work in
time.sleep(3)    #sleeps for 3 seconds

#lists all the colour wools as numbers(their ID's so the program can use it
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


def space_invader(colour):    #defines space_invader(colour)
    for location in(4,5,7,8):
        mc.setBlock(location,0,0,35,colour)    #uses for loops to place blocks that make a space invader and it does it in rows
    for location in(1,3,9,11):
        mc.setBlock(location,1,0,35,colour) #sets blocks at that location ans places the colour wool specified in the loop at the bottom and repeats to build the space invader
    for location in(1,3,4,5,6,7,8,9,11):
        mc.setBlock(location,2,0,35,colour)
    for location in(1,2,3,4,5,6,7,8,9,10,11):
        mc.setBlock(location,3,0,35,colour)
    for location in(2,3,5,6,7,9,10):
        mc.setBlock(location,4,0,35,colour)
    for location in(3,4,5,6,7,8,9):
        mc.setBlock(location,5,0,35,colour)
    for location in(4,8):
        mc.setBlock(location,6,0,35,colour)
    for location in(3,9):
        mc.setBlock(location,7,0,35,colour)
    time.sleep(0.20)
     #sleeps for 0.75 seconds and then will go through the same code again but for a different colour


    
while True: #creates an infinite loop
    for colour in(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15): # the id for each of the wool, the for looop goes through it and changes the colour to those
        space_invader(colour)   #makes the space invader change colour to the wool at the top




    























    




