
from pathlib import Path
import gui_menu
import webbrowser

from gse_gui import GSE_GUI

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class ContactGUI(GSE_GUI):
    def __init__(self, window) -> None:
        super(ContactGUI, self).__init__(window)

        # Contact Illustration
        self.illus_img = PhotoImage(
            file=self.relative_to_assets("contact_illus.png"))
        self.contact_illus = self.canvas.create_image(
            725.0,
            387.0,
            image=self.illus_img
        )

        # Contact title
        self.title_img = PhotoImage(
            file=self.relative_to_assets("contact_title.png"))
        self.contact_title = self.canvas.create_image(
            719.0,
            156.0,
            image=self.title_img
        )

        # Contact detail
        self.detail_img = PhotoImage(
            file=self.relative_to_assets("contact_details.png"))
        self.contact_detail = self.canvas.create_image(
            273.0,
            302.0,
            image=self.detail_img
        )

        # Form
        self.form_img = PhotoImage(
            file=self.relative_to_assets("btn__form.png"))
        self.form_btn = Button(
            image=self.form_img,
            borderwidth=0,
            background="#fff",
            highlightthickness=0,
            command=self.handle_form,
            relief="flat"
        )
        self.form_btn.place(
            x=198.0,
            y=391.0,
            width=67.0,
            height=19.0
        )

        self.canvas.create_rectangle(
            59.0,
            512.0,
            321.0,
            513.0,
            fill="#6E9DB6",
            outline="")

        # "Exit" BUTTON
        self.exit_img = PhotoImage(
            file=self.relative_to_assets("btn__exit_gray.png"))
        self.exit_btn = Button(
            image=self.exit_img,
            borderwidth=0,
            background="#fff",
            highlightthickness=0,
            command=self.handle_exit,
            relief="flat"
        )
        self.exit_btn.place(
            x=849.0,
            y=549.0,
            width=76.0,
            height=29.0
        )

    def handle_form(self):
        webbrowser.open("https://docs.google.com/forms/d/e/1FAIpQLSfsCBzftu9dVMe_dFVBh1xX0JSM-VHHgFwFFjmcrW4aPBYcEA/viewform?usp=sf_link")

if __name__ == '__main__':
    window = Tk()
    menu = ContactGUI(window)
    window.resizable(False, False)
    window.mainloop()