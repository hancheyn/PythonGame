from numpy import *
from PIL import Image, ImageTk
import random

class Player:
################################################################################################################
  def __init__(self, current_x, current_y, plr, skin, inventory):
    self.ply_x = current_x
    self.ply_y = current_y

    self.destination_x = current_x
    self.destination_y = current_y

    self.plrSize = plr
    #self.position = [{self.current_x}, {self.current_y}]
    self.animation_type = 0
    self.state = 0

    # Inventory
    self.inventory = inventory

    # PLAYERS
    img = Image.open("images/orangeshirt.png")
    resize_img = img.resize((self.plrSize, self.plrSize), Image.ANTIALIAS)
    self.orangeshirtTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/blueshirt.png")
    resize_img = img.resize((self.plrSize, self.plrSize), Image.ANTIALIAS)
    self.blueshirtTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/greenshirt.png")
    resize_img = img.resize((self.plrSize, self.plrSize), Image.ANTIALIAS)
    self.greenshirtTile = ImageTk.PhotoImage(resize_img)

    if skin != None:
      img = Image.open(skin + "-0.png")
      resize_img = img.resize((self.plrSize, self.plrSize), Image.ANTIALIAS)
      self.skin_0Tile = ImageTk.PhotoImage(resize_img)

      img = Image.open(skin + "-1.png")
      resize_img = img.resize((self.plrSize, self.plrSize), Image.ANTIALIAS)
      self.skin_1Tile = ImageTk.PhotoImage(resize_img)

      img = Image.open(skin + "-2.png")
      resize_img = img.resize((self.plrSize, self.plrSize), Image.ANTIALIAS)
      self.skin_2Tile = ImageTk.PhotoImage(resize_img)

      img = Image.open(skin + "-3.png")
      resize_img = img.resize((self.plrSize, self.plrSize), Image.ANTIALIAS)
      self.skin_3Tile = ImageTk.PhotoImage(resize_img)

################################################################################################################   
  def player_Animation(self):
    if self.state == 0:
      pic = self.skin_0Tile
      self.state += 1
    elif self.state == 1:
      pic = self.skin_1Tile
      self.state += 1
    elif self.state == 2:
      pic = self.skin_2Tile
      self.state += 1
    elif self.state == 3:
      pic = self.skin_3Tile
      self.state += 1
    elif self.state == 4:
      pic = self.skin_0Tile
      self.state += 1
    elif self.state == 5:
      pic = self.skin_1Tile
      self.state += 1
    elif self.state == 6:
      pic = self.skin_2Tile
      self.state += 1
    elif self.state == 7:
      pic = self.skin_3Tile
      self.state += 1
    elif self.state == 8:
      pic = self.skin_0Tile
      self.state += 1
    elif self.state == 9:
      pic = self.skin_3Tile
      self.state = 0
    return pic
################################################################################################################

################################################################################################################
  def player_destinationSet(self, destination_x, destination_y):
    self.destination_x = destination_x
    self.destination_y = destination_y
    return
################################################################################################################
  
  def npc_player(self):
    return self.blueshirtTile

  def player_locationSet(self, current_x, current_y):
    self.position[0] = current_x
    self.position[1] = current_y
    self.ply_x = current_x
    self.ply_y = current_y
    return

  def setNewPosition(self):
    choice = random.randrange(1,6)
    direction = None
    if choice == 1:
      #self.ply_x = self.ply_x + 1
      direction = "Up"
    elif choice == 2:
      #self.ply_x = self.ply_x - 1
      direction = "Down"
    elif choice == 3:
      #self.ply_y = self.ply_y + 1
      direction = "Left"
    elif choice == 4:
      #self.ply_y = self.ply_y - 1
      direction = "Right"
    return direction

  def player_locationGet(self):
    return self.position

################################################################################################################
  def player_KeyPress(self, map, gameheight, gamewidth, keypress):

    action = 0

    upTile = map.getCurrentTile(self.ply_x, self.ply_y-1)
    downTile = map.getCurrentTile(self.ply_x, self.ply_y+1)
    leftTile = map.getCurrentTile(self.ply_x-1, self.ply_y)
    rightTile = map.getCurrentTile(self.ply_x+1, self.ply_y)
    centerTile = map.getCurrentTile(self.ply_x, self.ply_y)
    upOverlayTile = map.getCurrentOverlayTile(self.ply_x, self.ply_y-1)
    downOverlayTile = map.getCurrentOverlayTile(self.ply_x, self.ply_y+1)
    leftOverlayTile = map.getCurrentOverlayTile(self.ply_x-1, self.ply_y)
    rightOverlayTile = map.getCurrentOverlayTile(self.ply_x+1, self.ply_y)
    moveMap = False

    # Example Movement
    if keypress == "Up":
      moveUp = False
      # Check for access
      if upTile["access"] == "True" and self.move_Overlay(upOverlayTile):
        moveUp = True
      if self.ply_y-1 < 3:
        moveMap = True
        self.reset_Destination()
        
      # Check terrian for type
      # Check for Item
      if moveUp:
        self.animation_type = 1
        if moveMap: 
          map.setNegativeCurrentMap(0,1)
          self.reset_Destination()
        else:
          self.ply_y = self.ply_y-1

    elif keypress == "Down":
      moveDown = False
      # Check for access
      if downTile["access"] == "True" and self.move_Overlay(downOverlayTile):
        moveDown = True
      if self.ply_y+1 == gameheight-3:
        moveMap = True
      if moveDown:
        self.animation_type = 2
        if moveMap:
          map.setPositiveCurrentMap(0,1)
          self.reset_Destination()
        else:
          self.ply_y = self.ply_y+1
      
    elif keypress == "Right":
      moveRight = False
      # Check for access
      if rightTile["access"] == "True" and self.move_Overlay(rightOverlayTile):
        moveRight = True
      if self.ply_x+1 == gamewidth-3:
        moveMap = True
      if moveRight:
        self.animation_type = 3
        if moveMap:
          map.setPositiveCurrentMap(1,0)
          self.reset_Destination()
        else:
          self.ply_x += 1

    elif keypress == "Left":
      moveLeft = False
      # Check for access
      if leftTile["access"] == "True" and self.move_Overlay(leftOverlayTile):
        moveLeft = True
      if self.ply_x-1 < 3:
        moveMap = True
      if moveLeft:
        self.animation_type = 4
        if moveMap:
          map.setNegativeCurrentMap(1,0)
          self.reset_Destination()
        else:
          self.ply_x -= 1
    
    elif keypress == "space":
      item = centerTile["Item"]
      centerTile["Item"] = None
      if item != None:
        print("Pickup")
        # Add Item to Player Inventory
        #self.inventory.append([item])
        self.inventory = item

    elif keypress == "Escape":
      action = 1
      
    
    elif keypress == "r":
      item = self.inventory
      print(self.inventory)
      centerTile["Item"] = item
      self.inventory = None

    return action
################################################################################################################

################################################################################################################
  def npcMove(self, map, gameheight, gamewidth, keypress):

    action = 0

    upTile = map.getCurrentTile(self.ply_x, self.ply_y-1)
    downTile = map.getCurrentTile(self.ply_x, self.ply_y+1)
    leftTile = map.getCurrentTile(self.ply_x-1, self.ply_y)
    rightTile = map.getCurrentTile(self.ply_x+1, self.ply_y)
    centerTile = map.getCurrentTile(self.ply_x, self.ply_y)
    upOverlayTile = map.getCurrentOverlayTile(self.ply_x, self.ply_y-1)
    downOverlayTile = map.getCurrentOverlayTile(self.ply_x, self.ply_y+1)
    leftOverlayTile = map.getCurrentOverlayTile(self.ply_x-1, self.ply_y)
    rightOverlayTile = map.getCurrentOverlayTile(self.ply_x+1, self.ply_y)
    moveMap = False

    # Example Movement
    if keypress == "Up":
      moveUp = False
      # Check for access
      if upTile["access"] == "True" and self.move_Overlay(upOverlayTile):
        moveUp = True
      if self.ply_y-1 < 3:
        moveMap = True
        self.reset_Destination()
        
      # Check terrian for type
      # Check for Item
      if moveUp:
        self.animation_type = 1
        self.ply_y = self.ply_y-1

    elif keypress == "Down":
      moveDown = False
      # Check for access
      if downTile["access"] == "True" and self.move_Overlay(downOverlayTile):
        moveDown = True
      if self.ply_y+1 == gameheight-3:
        moveMap = True
      if moveDown:
        self.animation_type = 2
        self.ply_y = self.ply_y+1
      
    elif keypress == "Right":
      moveRight = False
      # Check for access
      if rightTile["access"] == "True" and self.move_Overlay(rightOverlayTile):
        moveRight = True
      if self.ply_x+1 == gamewidth-3:
        moveMap = True
      if moveRight:
        self.animation_type = 3
        self.ply_x += 1

    elif keypress == "Left":
      moveLeft = False
      # Check for access
      if leftTile["access"] == "True" and self.move_Overlay(leftOverlayTile):
        moveLeft = True
      if self.ply_x-1 < 3:
        moveMap = True
      if moveLeft:
        self.animation_type = 4
        self.ply_x -= 1
    
    elif keypress == "space":
      item = centerTile["Item"]
      centerTile["Item"] = None
      if item != None:
        print("Pickup")
        # Add Item to Player Inventory
        self.inventory.append(item)

    elif keypress == "Escape":
      action = 1

    elif keypress == "r":
      item = self.inventory[0]
      print(item)
      centerTile["Item"] = item
      self.inventory[0] = None

    return action
################################################################################################################


################################################################################################################
  def move_Overlay(self, tile):
    if tile["terrain"] == "blank":
      out = True
    else:
      out = False
    return out
################################################################################################################

################################################################################################################
  def player_AnimationType(self, view, x_off, y_off):

    direction = None

    # IDLE STATE 
    if self.animation_type == 0:
      img_ply = self.skin_3Tile
      view.setObject_Overlay(self.ply_x, 0, self.ply_y, 0, img_ply)

      # Check if desination is set
      direction = self.player_IsMoving()
      #print("IDLE")
    elif self.animation_type == 1:
      #print("PLAYER UP")
      img_ply = self.player_Animation()
      animationState = self.state
      inverseState = 9 - animationState
      if animationState == 0:
        view.setObject_Overlay(self.ply_x, 0, self.ply_y, (animationState*-y_off), img_ply)
        self.animation_type = 0
      else:
        view.setObject_Overlay(self.ply_x, 0, self.ply_y+1, (animationState*-y_off), img_ply)

    elif self.animation_type == 2:
      #print("PLAYER DOWN")
      img_ply = self.player_Animation()
      animationState = self.state
      inverseState = 9 - animationState
      if animationState == 0:
        view.setObject_Overlay(self.ply_x, 0, self.ply_y, (animationState*y_off), img_ply)
        self.animation_type = 0
      else:
        view.setObject_Overlay(self.ply_x, 0, self.ply_y-1, (animationState*y_off), img_ply)

    elif self.animation_type == 3:
      #print("PLAYER RIGHT")
      img_ply = self.player_Animation()
      animationState = self.state
      inverseState = 9 - animationState
      if animationState == 0:
        view.setObject_Overlay(self.ply_x, (animationState*x_off), self.ply_y, 0, img_ply)
        self.animation_type = 0
      else:
        view.setObject_Overlay(self.ply_x-1, (animationState*x_off), self.ply_y, 0, img_ply)

    elif self.animation_type == 4:
      #print("PLAYER LEFT")
      img_ply = self.player_Animation()
      animationState = self.state
      inverseState = 9 - animationState
      if animationState == 0:
        view.setObject_Overlay(self.ply_x, (animationState*-x_off), self.ply_y, 0, img_ply)
        self.animation_type = 0
      else:
        view.setObject_Overlay(self.ply_x+1, (animationState*-x_off), self.ply_y, 0, img_ply)
    return direction
################################################################################################################

################################################################################################################
  def player_IsMoving(self):

    movement = None
    x_diff = 0
    y_diff = 0
    x_positive = True
    y_positive = True

    if self.ply_x != self.destination_x or self.ply_y != self.destination_y:
      if self.ply_x < self.destination_x:
        x_diff = self.ply_x - self.destination_x
        x_positive = True
      else:
        x_diff = self.destination_x - self.ply_x 
        x_positive = False

      if self.ply_y < self.destination_y:
        y_diff = self.ply_y - self.destination_y
        y_positive = True
      else:
        y_diff = self.destination_y - self.ply_y 
        y_positive = False

      if y_diff < x_diff:
        if y_positive:
          movement = "Down"
        elif not y_positive:
          movement = "Up"
      else:
        if x_positive:
          movement = "Right"
        elif not x_positive:
          movement = "Left"

    return movement
################################################################################################################

################################################################################################################
  def reset_Destination(self):
    self.destination_x = self.ply_x
    self.destination_y = self.ply_y
    return
################################################################################################################
