# Adventure 6: LinesCirclesAndSpheres.py

# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program shows how to create lines, spheres and circles in
# Minecraft using the MinecraftDrawing functions in minecraftstuff.


import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time

#create the minecraft api
mc = minecraft.Minecraft.create()

#create the minecraft drawing object
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

#get the players position
pos = mc.player.getTilePos()

#draw 3 lines
mcdrawing.drawLine(pos.x, pos.y, pos.z, 
                   pos.x, pos.y+20, pos.z, 
                   block.WOOL.id,1)
mcdrawing.drawLine(pos.x, pos.y, pos.z, 
                   pos.x+20, pos.y, pos.z, 
                   block.WOOL.id,2)
mcdrawing.drawLine(pos.x, pos.y, pos.z, 
                   pos.x + 20, pos.y + 20, pos.z, 
                   block.WOOL.id, 3)

#sleep so the player can move to a different position
time.sleep(5)

#draw a circle above the player
pos = mc.player.getTilePos()
mcdrawing.drawCircle(pos.x, pos.y + 20, pos.z, 20, block.WOOL.id, 4)
time.sleep(5)

#draw a sphere above the player
pos = mc.player.getTilePos()
mcdrawing.drawSphere(pos.x, pos.y + 20, pos.z, 15, block.WOOL.id, 5)
time.sleep(5)

