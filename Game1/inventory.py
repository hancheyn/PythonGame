from numpy import *
from PIL import Image, ImageTk


class Inventory:
  def __init__(self):    
    self.inventoryMatrix = array([[{"Item": None} for i in range(5)] for j in range(10)])

    # Images
    img = Image.open("images/path.png")
    resize_img = img.resize((50, 50), Image.ANTIALIAS)
    self.socket_image = ImageTk.PhotoImage(resize_img)

    self.bg_img = Image.open("images/stone_backgrounds.jpg")
    resize_img = self.bg_img.resize((1050, 750), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(resize_img)

    return

  def setInventory(self, view):
    for i in range(5):
      for j in range(5):
        view.setObject_Overlay(i+10, 0, j+5, 0, self.socket_image)
    return

  def setArmor(self, view):
    for i in range(4):
      for j in range(5):
        view.setObject_Overlay(i+16, 0, j+5, 0, self.socket_image)

    
    return

  def setBackground(self, view):
    resize_img = self.bg_img.resize((int(view.screen_width/2), int(view.screen_height/2)), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(resize_img)
    view.setObject_Overlay(7, 0, 3, 0, self.bg_image) 
    return