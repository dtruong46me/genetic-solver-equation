
from pathlib import Path

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import gui_menu
import gui_solver
import webbrowser
from gse_gui import GSE_GUI

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class How2UseGUI(GSE_GUI):
    def __init__(self, window) -> None:
        super(How2UseGUI, self).__init__(window)
        
        # Set invisble for "exit_btn"
        self.exit_btn.place_forget()

        # HelaX Logo
        self.logo_img = PhotoImage(
            file=self.relative_to_assets("helax__logo.png"))
        self.helax_logo = self.canvas.create_image(
            284.0,
            116.0,
            image=self.logo_img
        )

        # How2Use Illustration
        self.illus_img = PhotoImage(
            file=self.relative_to_assets("how2use_illus.png"))
        self.how2use_illus = self.canvas.create_image(
            258.0,
            355.0,
            image=self.illus_img
        )

        # How2Use title
        self.title_img = PhotoImage(
            file=self.relative_to_assets("how2use_title.png"))
        self.how2use_title = self.canvas.create_image(
            720.0,
            125.0,
            image=self.title_img
        )

        # How2Use detail
        self.detail_img = PhotoImage(
            file=self.relative_to_assets("how2use_details.png"))
        self.how2use_detail = self.canvas.create_image(
            711.0,
            359.0,
            image=self.detail_img
        )

        # "In here" BUTTON
        self.inhere_img = PhotoImage(
            file=self.relative_to_assets("btn__inhere.png"))
        self.inhere_btn = Button(
            image=self.inhere_img,
            borderwidth=0,
            highlightthickness=0,
            background="#fff",
            command=self.handle_inhere,
            relief="flat"
        )
        self.inhere_btn.place(
            x=536.0,
            y=348.0,
            width=52.0,
            height=19.0
        )

        # "Start now" BUTTON
        self.startnow_img = PhotoImage(
            file=self.relative_to_assets("btn__startnow.png"))
        self.startnow_btn = Button(
            image=self.startnow_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_startnow,
            relief="flat"
        )
        self.startnow_btn.place(
            x=778.0,
            y=524.0,
            width=142.0,
            height=46.0
        )
        self.startnow_btn.bind("<Return>", lambda event: self.handle_startnow())
        self.startnow_btn.focus_set()

    def handle_startnow(self):
        self.current_gui = None

        for widget in self.window.winfo_children():
            widget.destroy()

        self.solver_gui = gui_solver.SolverGUI(self.window)
        self.current_gui = self.solver_gui
    
    def handle_inhere(self):
        webbrowser.open("https://github.com/dtruong46me/genetic-solver-equation/blob/master/README.md#input-syntax")

if __name__ == '__main__':
    window = Tk()
    menu = How2UseGUI(window)
    window.resizable(False, False)
    window.mainloop()