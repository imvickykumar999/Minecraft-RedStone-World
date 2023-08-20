
# pip install mcpi
from mcpi.minecraft import Minecraft 

mc = Minecraft.create(address = 'localhost', port = 56531) 
mc.postToChat('Hello World')

# pos = mc.player.getPos()
# print(pos)
