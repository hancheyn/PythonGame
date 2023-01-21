from numpy import *
from PIL import Image, ImageTk

class Map:
################################################################################################################
  def __init__(self, tile, plr, current_x, current_y, game_width, game_height):
    #self.name = name
    #self.age = age

    self.game_width = game_width
    self.game_height = game_height

    self.tileSize = tile
    self.plrSize = plr

    # Viewable Portion of Map Top Left Tile
    self.current_x = current_x
    self.current_y = current_y

    # Initialize Tile Photos
    img = Image.open("images/grass.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.grassTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/trunk.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.trunkTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/wall.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.wallTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/path.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.pathTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/flowers.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.flowersTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/water.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.waterTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/roof.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.roofTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/window.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.windowTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/door.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.doorTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/tree.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.treeTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/treetop.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.treetopTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/treeleft.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.treeleftTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/treeright.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.treerightTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/treelefttop.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.treelefttopTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/treerighttop.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.treerighttopTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/treetop.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.treetopTile = ImageTk.PhotoImage(resize_img)

    # PLAYERS
    img = Image.open("images/orangeshirt.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.orangeshirtTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/blueshirt.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.blueshirtTile = ImageTk.PhotoImage(resize_img)

    img = Image.open("images/greenshirt.png")
    resize_img = img.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
    self.greenshirtTile = ImageTk.PhotoImage(resize_img)

    # Create Base Map Tiles
    self.map_base = array([[{"access": "False","terrain": "water","Item": None} for i in range(50)]])
    for i in range(49):
      self.map_base = append(self.map_base,[[{"access": "True","terrain": "grass","Item": None} for i in range(50)]],0)
    for i in range(50):
      self.map_base[i][0]["terrain"] = "water"
      self.map_base[i][0]["access"] = "False"
      self.map_base[49][i]["terrain"] = "water"
      self.map_base[49][i]["access"] = "False"
      self.map_base[i][49]["terrain"] = "water"
      self.map_base[i][49]["access"] = "False"
      self.map_base[i][49]["terrain"] = "water"
      self.map_base[i][49]["access"] = "False"

    # Create Map Overlay
    self.map_overlay = array([[{"access": "True","terrain": "blank","Item": None}for i in range(50)]])
    for i in range(49):
      self.map_overlay = append(self.map_overlay,[[{"access": "True","terrain": "blank","Item": None} for i in range(50)]],0)
    #for i in range(50):
    #  self.map_overlay[i][3]["terrain"] = "trunk"
    self.setTree(1, 2)

################################################################################################################

#FIX For Multiple Maps
################################################################################################################
  def getCurrentMap(self, tileType):

    pic = self.grassTile
    if tileType == "grass":
      pic = self.grassTile

    return pic
################################################################################################################

################################################################################################################
  def getCurrentTile(self, x, y):
    tile = self.map_base[y+self.current_y][x+self.current_x]
    #print(tile)
    return tile
################################################################################################################

################################################################################################################
  def getCurrentOverlayTile(self, x, y):
    tile = self.map_overlay[y+self.current_y][x+self.current_x]
    #print(tile)
    return tile
################################################################################################################

################################################################################################################
  def getCurrentTilePic(self, x, y):
    pic = None
    if x+self.current_x > -1 and y+self.current_y > -1 and \
       x+self.current_x < 50 and y+self.current_y < 50:
      tile = self.map_base[y+self.current_y][x+self.current_x]    
      picType = tile["terrain"]
      if picType == "grass":
        pic = self.grassTile
      elif picType == "water":
        pic = self.waterTile
      elif picType == "path":
        pic = self.pathTile
      elif picType == "tree":
        pic = self.treeTile
      elif picType == "wall":
        pic = self.wallTile   
    return pic

  def getCurrentTileOverlayPic(self, x, y):
    pic = None
    if x+self.current_x > -1 and y+self.current_y > -1 and \
       x+self.current_x < 50 and y+self.current_y < 50:
      tile = self.map_overlay[y+self.current_y][x+self.current_x]  
      picType = tile["terrain"]
      if picType == "grass":
        pic = self.grassTile
      elif picType == "water":
        pic = self.waterTile
      elif picType == "path":
        pic = self.pathTile
      elif picType == "tree":
        pic = self.treeTile
      elif picType == "trunk":
        pic = self.trunkTile
      elif picType == "treeleft":
        pic = self.treeleftTile
      elif picType == "treeright":
        pic = self.treerightTile
      elif picType == "treelefttop":
        pic = self.treelefttopTile
      elif picType == "treerighttop":
        pic = self.treerighttopTile
      elif picType == "treetop":
        pic = self.treetopTile
      elif picType == "trunk":
        pic = self.trunkTile
      elif picType == "wall":
        pic = self.wallTile
      elif picType == "door":
        pic = self.doorTile
      elif picType == "window":
        pic = self.windowTile
      elif picType == "roof":
        pic = self.roofTile
      elif picType == "door":
        pic = self.doorTile
      elif picType == "roof":
        pic = self.roofTile
    return pic

  def pickupItem(self, Tile):
    item = None
    # Store Item
    item = Tile["Item"]
    # Remove Item
    Tile["Item"] = None
    return item

  def setPositiveCurrentMap(self, x, y):
    self.current_x += x
    self.current_y += y
    return

  def setNegativeCurrentMap(self, x, y):
    self.current_x -= x
    self.current_y -= y
    return

  def setTree(self, x, y):
    self.map_overlay[3+y][2+x]["terrain"] = "trunk"
    self.map_overlay[1+y][1+x]["terrain"] = "treelefttop"
    self.map_overlay[1+y][3+x]["terrain"] = "treerighttop"
    self.map_overlay[2+y][1+x]["terrain"] = "treeleft"
    self.map_overlay[2+y][2+x]["terrain"] = "tree"
    self.map_overlay[2+y][3+x]["terrain"] = "treeright"
    self.map_overlay[1+y][2+x]["terrain"] = "treetop"

  def setHouse(self, x, y):
    self.map_overlay[1+y][1+x]["terrain"] = "roof"
    self.map_overlay[1+y][3+x]["terrain"] = "roof"
    self.map_overlay[2+y][1+x]["terrain"] = "wall"
    self.map_overlay[2+y][2+x]["terrain"] = "door"
    self.map_overlay[2+y][3+x]["terrain"] = "wall"
    self.map_overlay[1+y][2+x]["terrain"] = "roof"

  def setItem(self, x, y, item):
    self.map_base[y][x]["Item"] = item
    return

################################################################################################################

