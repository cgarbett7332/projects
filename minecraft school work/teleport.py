### Basic Teleporter in Minecraft-pi

import time,mcpi.minecraft as mc #adds mcpi modules
game = mc.Minecraft.create() #connects to a minecraft game and calls it game

time.sleep(2.5)
game.postToChat("welcome to the world of mianite!")
time.sleep(3)
game.postToChat("i am GOD")
time.sleep(2)
game.player.setPos(70,70,70)
time.sleep(2)
game.postToChat("hahaha :)")


