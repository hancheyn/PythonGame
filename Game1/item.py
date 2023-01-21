from numpy import *
from PIL import Image, ImageTk

class Item:

  def __init__(self, name, pic):
    self.name = name
    self.item_pic = pic

    # Item Properties
    self.weight = 0
    self.dexterity = 0


  def showItem(self):
    return self.item_pic