import sys
import os

from tkinter import Tk

path = os.path.dirname(__file__)

sys.path.insert(0, path)

from src.gui.gui_menu import MenuGUI

if __name__ == '__main__':
    window = Tk()
    menu = MenuGUI(window)
    window.resizable(False, False)
    window.mainloop()