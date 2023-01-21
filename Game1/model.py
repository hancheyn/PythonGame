from numpy import *
from PIL import Image, ImageTk

import map
import item
import player
import inventory

class Model:
################################################################################################################
  def __init__(self, current_x, current_y):
    self.current_x = current_x
    self.current_y = current_y
    

################################################################################################################

  def init_map(self, x, y, game_width, game_height):
    self.map = map.Map(x, y, self.current_x, self.current_y, game_width, game_height)
    self.game_width = game_width
    self.game_height = game_height
    self.setMapOverlay()

  def init_player(self):
    self.player = player.Player(4, 4, 80, "images/pangwizard", self.inventory)
    b = self.init_belt()

  def init_items(self):

    # Images
    img = Image.open("images/path.png")
    resize_img = img.resize((50, 50), Image.ANTIALIAS)
    self.socket_image = ImageTk.PhotoImage(resize_img)
    
    # Bone Image
    img = Image.open("images/bone.png")
    resize_img = img.resize((100, 100), Image.ANTIALIAS)
    self.bone_image = ImageTk.PhotoImage(resize_img)
    new_item = item.Item("Bone", self.bone_image)
    print(new_item)
    self.bone_item = new_item
    return

  def init_npc(self):
    self.npc_player = player.Player(4, 4, 80, None, None)
    self.npc_player2 = player.Player(4, 5, 80, None, None)
    self.npc_player3 = player.Player(4, 6, 80, None, None)

    self.npcArray = array([self.npc_player, self.npc_player2, self.npc_player3])
    return

# Player Interface

  def init_inventory(self):
    self.inventory = inventory.Inventory()

  def init_belt(self):
    img = Image.open("images/belt.png")
    resize_img = img.resize((500, 500), Image.ANTIALIAS)
    self.belt_image = ImageTk.PhotoImage(resize_img)
    return self.belt_image
  
  def setInventory(self, view):
    self.inventory.setBackground(view)
    self.inventory.setInventory(view)
    self.inventory.setArmor(view)
    return

# End of Player Interface
  def getGrass(self):
    return self.map.getCurrentMap("grass")

################################################################################################################
# Items are part of Overlay Init
  def setMapOverlay(self): 
    self.map.setTree(1, 2)
    self.map.setTree(13, 5)
    self.map.setTree(30, 20)
    self.map.setTree(20, 10)
    self.map.setTree(10, 30)
    self.map.setTree(30, 30)
    self.map.setTree(40, 20)
    self.map.setTree(20, 40)
    self.map.setHouse(6, 4)

    # Set Item
    bone = self.bone_item
    self.map.setItem(5, 11, bone)
################################################################################################################

