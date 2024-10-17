"""
PROJECT: SLIDING PUZZLE GAME

    This is a 4*4 sliding puzzle game which is implemented in Python
    ... to be implemented in Rust later
    
Interface:
    GUI using Tkinter/Pygame
    
Author: Joseph Junior Mensah
"""

from tkinter import *
from PIL import Image, ImageTk

root = Tk()

window_properties = {
    'root':root,
    'WIN_WIDTH':640,
    'WIN_HEIGHT':640,
    'THEME_DARK':'#283A73',
    'THEME_LIGHT':'#ccc',
    'DEFAULT_FONT':'montserrat',
    'DEFAULT_FONT_SIZE':10,
}

# WINDOW SETUP
root.title("SLIDING PUZZLE GAME")
root.iconbitmap("image/sliding_puzzle_game_icon.ico")
root.geometry(f"{window_properties['WIN_WIDTH']}x{window_properties['WIN_HEIGHT']}")
root.configure(bg=window_properties['THEME_LIGHT'])
root.resizable(False,False)

root = window_properties['root']

"""
TINKERING CODE - Using tiles as an example
#Tiles in Row 1
tile1 = Frame(root, bg=window_properties['THEME_LIGHT'])
tile1.place(x = 0, y = 0, width = ((window_properties['WIN_WIDTH'])/4), height = ((window_properties['WIN_HEIGHT'])/4))

tile2 = Frame(root, bg=window_properties['THEME_DARK'])
tile2.place(x = ((window_properties['WIN_WIDTH'])/4), y = 0, width = (window_properties['WIN_WIDTH'])/4, height = (window_properties['WIN_HEIGHT'])/4)

tile3 = Frame(root, bg=window_properties['THEME_LIGHT'])
tile3.place(x = 2 * ((window_properties['WIN_WIDTH'])/4), y = 0, width = (window_properties['WIN_WIDTH'])/4, height = (window_properties['WIN_HEIGHT'])/4)

tile4 = Frame(root, bg=window_properties['THEME_DARK'])
tile4.place(x = 3 * ((window_properties['WIN_WIDTH'])/4), y = 0, width = (window_properties['WIN_WIDTH'])/4, height = (window_properties['WIN_HEIGHT'])/4)

#Tiles in Row 2
tile5 = Frame(root, bg=window_properties['THEME_DARK'])
tile5.place(x = 0, y = ((window_properties['WIN_WIDTH'])/4), width = ((window_properties['WIN_WIDTH'])/4), height = ((window_properties['WIN_HEIGHT'])/4))

tile6 = Frame(root, bg=window_properties['THEME_LIGHT'])
tile6.place(x = ((window_properties['WIN_WIDTH'])/4), y = ((window_properties['WIN_WIDTH'])/4), width = (window_properties['WIN_WIDTH'])/4, height = (window_properties['WIN_HEIGHT'])/4)

tile7 = Frame(root, bg=window_properties['THEME_DARK'])
tile7.place(x = 2 * ((window_properties['WIN_WIDTH'])/4), y = ((window_properties['WIN_WIDTH'])/4), width = (window_properties['WIN_WIDTH'])/4, height = (window_properties['WIN_HEIGHT'])/4)

tile8 = Frame(root, bg=window_properties['THEME_LIGHT'])
tile8.place(x = 3 * ((window_properties['WIN_WIDTH'])/4), y = ((window_properties['WIN_WIDTH'])/4), width = (window_properties['WIN_WIDTH'])/4, height = (window_properties['WIN_HEIGHT'])/4)

#Tiles in Row 3
tile9 = Frame(root, bg=window_properties['THEME_LIGHT'])
tile9.place(x = 0, y = 2 * ((window_properties['WIN_WIDTH'])/4), width = ((window_properties['WIN_WIDTH'])/4), height = ((window_properties['WIN_HEIGHT'])/4))

tile10 = Frame(root, bg=window_properties['THEME_DARK'])
tile10.place(x = ((window_properties['WIN_WIDTH'])/4), y = 2 * ((window_properties['WIN_WIDTH'])/4), width = (window_properties['WIN_WIDTH'])/4, height = (window_properties['WIN_HEIGHT'])/4)

tile11 = Frame(root, bg=window_properties['THEME_LIGHT'])
tile11.place(x = 2 * ((window_properties['WIN_WIDTH'])/4), y = 2 * ((window_properties['WIN_WIDTH'])/4), width = (window_properties['WIN_WIDTH'])/4, height = (window_properties['WIN_HEIGHT'])/4)

tile12 = Frame(root, bg=window_properties['THEME_DARK'])
tile12.place(x = 3 * ((window_properties['WIN_WIDTH'])/4), y = 2 * ((window_properties['WIN_WIDTH'])/4), width = (window_properties['WIN_WIDTH'])/4, height = (window_properties['WIN_HEIGHT'])/4)

#Tiles in Row 4
tile13 = Frame(root, bg=window_properties['THEME_DARK'])
tile13.place(x = 0, y = 3 * ((window_properties['WIN_WIDTH'])/4), width = ((window_properties['WIN_WIDTH'])/4), height = ((window_properties['WIN_HEIGHT'])/4))

tile14 = Frame(root, bg=window_properties['THEME_LIGHT'])
tile14.place(x = ((window_properties['WIN_WIDTH'])/4), y = 3 * ((window_properties['WIN_WIDTH'])/4), width = (window_properties['WIN_WIDTH'])/4, height = (window_properties['WIN_HEIGHT'])/4)

tile15 = Frame(root, bg=window_properties['THEME_DARK'])
tile15.place(x = 2 * ((window_properties['WIN_WIDTH'])/4), y = 3 * ((window_properties['WIN_WIDTH'])/4), width = (window_properties['WIN_WIDTH'])/4, height = (window_properties['WIN_HEIGHT'])/4)

tile16 = Frame(root, bg=window_properties['THEME_LIGHT'])
tile16.place(x = 3 * ((window_properties['WIN_WIDTH'])/4), y = 3 * ((window_properties['WIN_WIDTH'])/4), width = (window_properties['WIN_WIDTH'])/4, height = (window_properties['WIN_HEIGHT'])/4)
"""

"""
TINKERING - Using an actual image
puzzle_image = ImageTk.PhotoImage(Image.open("image/jjmensah.jpg").resize(((window_properties['WIN_WIDTH']),(window_properties['WIN_HEIGHT']))).crop((0,0,(window_properties['WIN_WIDTH'] / 4),(window_properties['WIN_HEIGHT'] / 4))))
puzzle_image_label = Label(root, text = "Tile 1", bg = window_properties['THEME_DARK'], fg = window_properties['THEME_LIGHT'], image = puzzle_image)
puzzle_image_label.place(x = 0, y = 0)

"""

#Tile def
tile = Frame(root, bg=window_properties['THEME_LIGHT'])
tile.place(x = 0, y = 0, width = ((window_properties['WIN_WIDTH'])/4), height = ((window_properties['WIN_HEIGHT'])/4))

#Matrix definition to set up 4*4 cropped images of full_image
frame_array = []
t_array = []
t_complement_array = []
label_array = []

index = 0

for i in range(4):
    for j in range(4):
        frame_array.append(Frame(tile))
        
        if (i == 3) and (j == 3):
            label_array.append(Label(frame_array[index], background = "#00fg"))
            t_array.append(["", index])
            t_complement_array.append(["", index])
        else:
            # 160 is equivalent to width (640) / 4 or height (640) / 4
            t_array.append([ImageTk.PhotoImage(Image.open("image/jjmensah.jpg").resize(((window_properties['WIN_WIDTH']),(window_properties['WIN_HEIGHT']))).crop(((i * 160), (j * 160), (i * 160) + 160, (j * 160) + 160))), index])
            t_complement_array.append([ImageTk.PhotoImage(Image.open("image/jjmensah.jpg").resize(((window_properties['WIN_WIDTH']),(window_properties['WIN_HEIGHT']))).crop(((i * 160), (j * 160), (i * 160) + 160, (j * 160) + 160))), index])
            label_array.append(Label(frame_array[index], image = t_array[index][0]), background = "#3b53a0")
        
        label_array[index].bind("<Button-1>", lambda event,h = index:func_1(event,h)) #Function definition of func_1 to create an instance









root.mainloop()