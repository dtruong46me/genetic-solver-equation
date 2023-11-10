
from tkinter import Tk

from gui_menu import MenuGUI
from gui_solver import SolverGUI

class GeneticSolverApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x600")
        self.window.configure(bg="#FFF")

        self.menu_gui = MenuGUI(window)
        self.current_gui = self.menu_gui
    
    # Switch to Solver GUI
    def handle_start(self):
        self.current_gui = None

        for widget in self.window.winfo_children():
            widget.destroy()

        self.solver_gui = SolverGUI(self.window)
        self.current_gui = self.solver_gui

    # Switch to Menu GUI
    def switch_to_menu(self):
        self.current_gui = None
        for widget in self.window.winfo_children():
            widget.destroy()

        self.menu_gui = MenuGUI(self.window)
        self.current_gui = self.menu_gui

if __name__ == '__main__':
    window = Tk()
    main_gui = GeneticSolverApp(window)
    window.mainloop()