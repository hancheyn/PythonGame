################################################################################################################
# Pass the view to the controller to update states in the view
import time
import signal

# IF NEEDED?
import random
import multiprocessing
from playsound import playsound

class Controller:
################################################################################################################
  def __init__(self, model, start_x, start_y):
    self.model = model
    self.ply_x = start_x
    self.ply_y = start_y
    self.game_height = 0
    self.game_width = 0
    self.animation_state = 0
    self.freeze_screen = False

    return
################################################################################################################

################################################################################################################
  def gameSetup(self, game_width, game_height, view):
    self.game_height = game_height
    self.game_width = game_width
    self.view = view
    self.model.init_belt()
   
    view.setObject_Permanent(710,700,self.model.belt_image )
################################################################################################################

################################################################################################################
  # Control User Inputs and States
  def control_motion(self, event, view):
    #print("Mouse position: (%s %s)" % (event.x, event.y))
    return
################################################################################################################

################################################################################################################
  def control_leftclick(self, event, view):
    print("Mouse leftclick: (%s %s)" % (event.x, event.y))
    
    # Determine Tile Coordinate
    xcoord = (event.x-self.view.map_originx) / self.view.gridx
    ycoord = (event.y-self.view.map_originy) / self.view.gridy
    print("Tile: (%s %s)" % (int(xcoord), int(ycoord)))

    # Set Destination
    self.model.player.player_destinationSet(int(xcoord), int(ycoord))

    # Start State Machine to Walk to Destination  
    # Cyclic Check if destination = current location
    return
################################################################################################################

################################################################################################################
  def control_click(self, event, view):
    print("Mouse click: (%s %s)" % (event.x, event.y))

    # Add a Sound
    self.p = multiprocessing.Process(target=playsound, args=('http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3',))
    self.p.start()

    return
################################################################################################################

################################################################################################################
  def control_key(self, event, view):
    print("Key press: (%s)" % (event))

    action = self.model.player.player_KeyPress(self.model.map, self.game_height, self.game_width, event.keysym)
    if action == 1:
      if view.screen_fade:
        view.screen_fade = False
      else:
        view.screen_fade = True
        pic = self.model.player.inventory.item_pic
        self.view.setObject_Overlay(5, 0, 5, 0, pic)

    self.model.player.reset_Destination()

    return

  #N/A ?
  def set_player(self, view):
    img_ply = self.model.player.player_Animation()
    view.setObject_Overlay(self.ply_x, 0, self.ply_y, 0, img_ply)
    return
################################################################################################################

################################################################################################################
  def timeout_handler(self):
    print("Cyclic Init!")

    return
################################################################################################################

################################################################################################################
  def cyclic25_handler(self):
    x_off = self.view.gridx/10
    y_off = self.view.gridy/10
    if not self.freeze_screen:
      direction = self.model.player.player_AnimationType(self.view, x_off, y_off)
      if direction != None:
        self.model.player.player_KeyPress(self.model.map, self.game_height, self.game_width, direction)

      # RESET OBJECT IMAGES
      # Reset NPCs
      image = self.model.npc_player.npc_player()
      for i in range(len(self.model.npcArray)):
        self.view.setObject_Overlay(self.model.npcArray[i].ply_x, 0, self.model.npcArray[i].ply_y, 0, image)
      
      if self.view.screen_fade:
        self.freeze_screen = True
        self.model.setInventory(self.view)
      self.view.resetScreen()

    if not self.view.screen_fade:
      self.freeze_screen = False
        
    return
################################################################################################################

################################################################################################################
  def cyclic1_handler(self):

    if not self.freeze_screen:
      # Loop for NPC's
      for i in range(len(self.model.npcArray)):
        image = self.model.npcArray[i].npc_player()
        position = self.model.npcArray[i].setNewPosition()
        self.model.npcArray[i].npcMove(self.model.map, self.game_height, self.game_width, position)
        self.view.setObject_Overlay(self.model.npcArray[i].ply_x, 0, self.model.npcArray[i].ply_y, 0, image)
    
    if self.view.screen_fade:
      self.freeze_screen = True
    else:
      self.freeze_screen = False
    return
################################################################################################################

