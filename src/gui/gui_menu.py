
from pathlib import Path
import webbrowser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import gui_solver
import gui_contact
import gui_about
import gui_how2use
from gse_gui import GSE_GUI

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

class MenuGUI(GSE_GUI):
    def __init__(self, window) -> None:
        super(MenuGUI, self).__init__(window)

        # Set invisible for "backhome_btn"
        self.backhome_btn.place_forget()

        # HelaX LOGO
        self.logo_img = PhotoImage(
            file=self.relative_to_assets("helax__logo.png"))
        self.logo = self.canvas.create_image(
            157.0,
            48.0,
            image=self.logo_img
        )

        # Welcome to GSE App
        self.gse_img = PhotoImage(
            file=self.relative_to_assets("genetic_solver_eqt.png"))
        self.gse_text = self.canvas.create_image(
            287.0,
            225.0,
            image=self.gse_img
        )

        # "How to use" BUTTON
        self.how_to_use_img = PhotoImage(
            file=self.relative_to_assets("btn__how_to_use.png"))
        self.how_to_use_btn = Button(
            image=self.how_to_use_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_how_to_use,
            relief="flat"
        )
        self.how_to_use_btn.place(x=125.0, y=331.0, width=146.0, height=53.0)

        # "Start" BUTTON
        self.start_img = PhotoImage(
            file=self.relative_to_assets("btn__start.png"))
        self.start_btn = Button(
            image=self.start_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_start,
            relief="flat"
        )
        self.start_btn.place(
            x=304.0,
            y=331.0,
            width=146.0,
            height=53.0
        )
        self.start_btn.bind("<Return>", lambda event: self.handle_start())
        self.start_btn.focus_set()

        # HelaX BOT
        self.bot_img = PhotoImage(
            file=self.relative_to_assets("helax__bot.png"))
        self.helax_bot = self.canvas.create_image(
            730.0,
            333.0,
            image=self.bot_img
        )

        # "About" BUTTON
        self.about_img = PhotoImage(
            file=self.relative_to_assets("btn__about.png"))
        self.about_btn = Button(
            image=self.about_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_about,
            relief="flat"
        )
        self.about_btn.place(
            x=651.0,
            y=17.0,
            width=94.0,
            height=59.0
        )

        # "FAQs" BUTTON
        self.faqs_img = PhotoImage(
            file=self.relative_to_assets("btn__faqs.png"))
        self.faqs_btn = Button(
            image=self.faqs_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_faqs,
            relief="flat"
        )
        self.faqs_btn.place(
            x=745.0,
            y=17.0,
            width=85.0,
            height=59.0
        )

        # "Contact" BUTTON
        self.contact_img = PhotoImage(
            file=self.relative_to_assets("btn__contact.png"))
        self.contact_btn = Button(
            image=self.contact_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_contact,
            relief="flat"
        )
        self.contact_btn.place(
            x=830.0,
            y=17.0,
            width=110.0,
            height=59.0
        )
    
    def handle_how_to_use(self):
        self.current_gui = None

        for widget in self.window.winfo_children():
            widget.destroy()

        self.how2use_gui = gui_how2use.How2UseGUI(self.window)
        self.current_gui = self.how2use_gui
    
    def handle_start(self):
        self.current_gui = None

        for widget in self.window.winfo_children():
            widget.destroy()

        self.solver_gui = gui_solver.SolverGUI(self.window)
        self.current_gui = self.solver_gui

    def handle_about(self):
        self.current_gui = None

        for widget in self.window.winfo_children():
            widget.destroy()

        self.about_gui = gui_about.AboutGUI(self.window)
        self.current_gui = self.about_gui
    
    def handle_faqs(self):
        print()

    def handle_contact(self):
        self.current_gui = None

        for widget in self.window.winfo_children():
            widget.destroy()

        self.contact_gui = gui_contact.ContactGUI(self.window)
        self.current_gui = self.contact_gui
    
if __name__ == '__main__':
    window = Tk()
    menu = MenuGUI(window)
    window.resizable(False, False)
    window.mainloop()
