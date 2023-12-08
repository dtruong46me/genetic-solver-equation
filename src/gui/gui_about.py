
from pathlib import Path
import gui_menu
import webbrowser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from gse_gui import GSE_GUI

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class AboutGUI(GSE_GUI):
    def __init__(self, window) -> None:
        super().__init__(window)
    
        # About Illustration
        self.illus_img = PhotoImage(
            file=self.relative_to_assets("about_illus.png"))
        self.about_illus = self.canvas.create_image(
            280.0,
            322.0,
            image=self.illus_img
        )

        # About title
        self.title_img = PhotoImage(
            file=self.relative_to_assets("about_title.png"))
        self.about_title = self.canvas.create_image(
            716.0,
            170.0,
            image=self.title_img
        )

        # About detail
        self.detail_img = PhotoImage(
            file=self.relative_to_assets("about_details.png"))
        self.about_detail = self.canvas.create_image(
            730.0,
            401.0,
            image=self.detail_img
        )

if __name__ == '__main__':
    window = Tk()
    menu = AboutGUI(window)
    window.resizable(False, False)
    window.mainloop()