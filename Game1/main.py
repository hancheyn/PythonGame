import tkinter as tk
import time

import view
import controller
import model

################################################################################################################
# MAIN Setup

# Init Maps and Game Classes in Model
m = model.Model(1, 0)

# Controller gets called by view after input
c = controller.Controller(m, 4, 4)

# View Carries the Screen Output  
v = view.View(c)
################################################################################################################

################################################################################################################
# Start Game
v.setup_events()
v.setup_window(30,16)
################################################################################################################
