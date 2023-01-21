import tkinter as tk
from numpy import *
from PIL import Image, ImageTk

# Try Canvas
# https://www.tutorialspoint.com/python/tk_canvas.htm
# Aspect ration 16;9

class View:
################################################################################################################
  def __init__(self, controller):

    self.controller = controller

    # Setup Window
    self.window = tk.Tk()
    self.window.wm_title("Game Tester")
    #self.window.attributes('-fullscreen', True)
    #self.window.config(cursor="none")
    self.window.configure(background="black")
    self.screen_width = self.window.winfo_screenwidth()
    self.screen_height = self.window.winfo_screenheight()
    self.window.geometry(f'{self.screen_width}x{self.screen_height}')

    # Setup Frame
    self.frame = tk.Frame(self.window)
    self.frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
    self.frame.configure(background="black")

    # Setup Canvas
    self.game_width = 28
    self.game_height = 14
    self.map_originx = 20
    self.map_originy = 20
    self.c = tk.Canvas(self.frame)
    self.c.pack(fill="both", expand=True)

    # Set Image
    self.img= Image.open("images/grass.png")
    self.gridx = self.screen_width/32
    self.gridy = self.screen_height/18
    self.resize_img = self.img.resize((int(self.gridx),int(self.gridy)), Image.ANTIALIAS)
    self.fimg= ImageTk.PhotoImage(self.resize_img)

    #Test Image
    img1 = Image.open("images/orangeshirt.png")
    resize_img1 = img1.resize((int(self.gridx), int(self.gridy)), Image.ANTIALIAS)
    self.orangeshirtTile = ImageTk.PhotoImage(resize_img1)

    # Background Fade
    self.screen_fade = False
    fade = Image.open("images/fade.png")
    resize_fade = fade.resize((int(self.screen_width), int(self.screen_height)), Image.ANTIALIAS)
    self.fadeBG = ImageTk.PhotoImage(resize_fade)

    img = Image.open("images/stone_backgrounds.jpg")
    resize_img = img.resize((1050, 750), Image.ANTIALIAS)
    self.invBG = ImageTk.PhotoImage(resize_img)

    #BELT
    img = Image.open("images/belt.png")
    resize_img = img.resize((500, 500), Image.ANTIALIAS)
    self.belt_image = ImageTk.PhotoImage(resize_img)

    # Initialize Overlay
    self.object_overlay = array([{"xcoord": 0,"xoffset": 0,"ycoord": 0,"yoffset": 0,"image": None}])
    self.object_permanent = array([{"xcoord": 0,"ycoord": 0,"image": None}])

    self.setup_events()
################################################################################################################

################################################################################################################
  # Sets Up Screen Grid
  # Note: Set screen to adjust to center based on grid dimensions
  def setScreen(self,x,y):
    #Reset Canvas
    self.c.delete('all')
    self.game_width = x
    self.game_height = y
    
    bg = self.c.create_polygon(0, 0, self.screen_width, 0, self.screen_width, self.screen_height, 0, self.screen_height, fill="black")
    gridx = self.screen_width/32
    gridy = self.screen_height/18
    self.map_originx = ((31-x)/2)*gridx
    self.map_originy = ((17-y)/2)*gridy

    # Loop through Map Tiles
    for i in range(x):
        for j in range(y):
            # Setup
            xorigin = i*gridx + self.map_originx
            yorigin = j*gridy + self.map_originy
            nimg = self.controller.model.map.getCurrentTilePic(i,j)
            overlay_img = self.controller.model.map.getCurrentTileOverlayPic(i,j)

            # Get Tile Info
            current_tile = self.controller.model.map.getCurrentTile(i, j)

            # Check / Set Item
            if not self.screen_fade:
              current_item = current_tile["Item"]
              if current_item != None:
                self.setObject_Overlay(i,0,j,0,current_item.showItem())

            # Create Canvas Image
            if nimg != None:
              image = self.c.create_image(xorigin, yorigin, anchor=tk.NW, image=nimg)           
            if overlay_img != None:
              image2 = self.c.create_image(xorigin, yorigin, anchor=tk.NW, image=overlay_img)

    # Fade Map Option
    if self.screen_fade:
      self.fadeMap()

    # Loop through Object Overlays
    for i in range(len(self.object_overlay)):
      if i != 0:
        current_object = self.object_overlay[i]
        self.setObject(current_object["xcoord"], current_object["xoffset"], current_object["ycoord"], current_object["yoffset"], current_object["image"])

    # Loop through Permanent Objects
    for i in range(len(self.object_permanent)):
      permanent_object = self.object_permanent[i]
      perm_image = self.c.create_image(permanent_object["xcoord"], permanent_object["ycoord"], anchor=tk.NW, image=permanent_object["image"])

    #TEST BELT   
    #self.c.create_image(710, 700, anchor=tk.NW, image=self.belt_image)

    self.c.pack()
    del self.object_overlay
    #del self.object_permanent
    self.object_overlay = array([{"xcoord": 0,"xoffset": 0,"ycoord": 0,"yoffset": 0,"image": None}])
    #self.object_permanent = array([{"xcoord": 0,"ycoord": 0,"image": None}])
################################################################################################################

################################################################################################################
  def resetScreen(self):
    self.setScreen(self.game_width,self.game_height)
################################################################################################################

################################################################################################################
  def setPlayer(self, x, y):
    self.setScreen(self.game_width,self.game_height)
    gridx = self.screen_width/32
    gridy = self.screen_height/18
    xorigin = x*gridx + self.map_originx
    yorigin = y*gridy + self.map_originy    
    player = self.c.create_image(xorigin, yorigin, anchor=tk.NW, image=self.orangeshirtTile)
    self.c.pack()
################################################################################################################

################################################################################################################
  def setObject(self, x, x_offset, y, y_offset, pic):
    #self.resetScreen()
    gridx = self.screen_width/32
    gridy = self.screen_height/18
    xorigin = x*gridx + self.map_originx
    yorigin = y*gridy + self.map_originy

    player = self.c.create_image(xorigin+x_offset, yorigin+y_offset, anchor=tk.NW, image=pic)
    self.c.pack()
################################################################################################################

################################################################################################################
  def setObject_Overlay(self, x, x_offset, y, y_offset, pic):
    self.object_overlay = append(self.object_overlay,[{"xcoord": x,"xoffset": x_offset,"ycoord": y,"yoffset": y_offset,"image": pic}],0)
    return
################################################################################################################

################################################################################################################
  def setObject_Permanent(self, x, y, pic):
    self.object_permanent = append(self.object_overlay,[{"xcoord": x,"ycoord": y,"image": pic}],0)
    return
################################################################################################################

################################################################################################################
  def resume_window(self,x,y):
    self.controller.timeout_handler()
    self.resume_window(x,y)
################################################################################################################

################################################################################################################
  # Sets Up User Inputs & Interrupts
  def get_entry(self):
    self.controller.timeout_handler()
    self.window.after(100, self.cyclic_25ms)
    self.window.after(100, self.cyclic_1s)
    return

  def cyclic_25ms(self):
    self.controller.cyclic25_handler()
    self.window.after(25, self.cyclic_25ms)

  def cyclic_1s(self):
    self.controller.cyclic1_handler()
    self.window.after(1000, self.cyclic_1s)


  def motion(self, event):
    self.controller.control_motion(event, self)
    return

  def key(self, event):
    self.controller.control_key(event, self)
    return

  def leftclick(self, event):
    self.controller.control_leftclick(event, self)
    return
  
  def rightclick(self, event):
    self.controller.control_click(event, self)
    return

  def redraw(self, event):
    self.screen_width = self.window.winfo_screenwidth()
    self.screen_height = self.window.winfo_screenheight()
    self.c.pack()
    
  def setup_events(self):
    # Setup User Input
    self.window.bind('<Motion>',self.motion)
    self.window.bind('<Key>',self.key)
    self.window.bind('<ButtonRelease-1>',self.leftclick)
    self.window.bind('<ButtonRelease-3>',self.rightclick)
    self.c.bind("<Configure>", self.redraw)
    return
################################################################################################################

################################################################################################################
  def setup_window(self,x,y):
    # Startup Settings
    self.controller.gameSetup(x, y, self)
    self.controller.model.init_items()
    self.controller.model.init_map(int(self.gridx),int(self.gridy),x,y)
    self.controller.model.init_inventory()
    self.controller.model.init_player()
    self.controller.model.init_npc()
    self.window.after(100, self.get_entry)
    self.setScreen(x,y)
    self.controller.set_player(self)
    self.window.mainloop()
################################################################################################################

################################################################################################################
  def getGameHeight():
    return self.game_height
################################################################################################################

################################################################################################################
  def getGameWidth():
    return self.game_width
################################################################################################################

  def fadeMap(self):
    #Image to fade map self.invBG
    self.c.create_image(0, 0, anchor=tk.NW, image=self.fadeBG)
    return
