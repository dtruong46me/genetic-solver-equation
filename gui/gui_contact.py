
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class ContactGUI:
    def __init__(self, window) -> None:
        # Handle assets file path
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path(r"../assets")

        self.window = window

        self.window.geometry("1000x600")
        self.window.configure(bg="#FFF")
        self.window.title("Genetic Solver Equation")

        self.canvas = Canvas(
            window,
            bg = "#FFF",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        # Back to Home
        self.backhome_img = PhotoImage(
            file=self.relative_to_assets("btn__back_home.png"))
        self.backhome_btn = Button(
            image=self.backhome_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_backhome,
            relief="flat"
        )
        self.backhome_btn.place(
            x=61.0,
            y=17.0,
            width=171.0,
            height=52.0
        )

        # HelaX Logo
        self.logo_img = PhotoImage(
            file=self.relative_to_assets("helax__logo.png"))
        self.helax_logo = self.canvas.create_image(
            284.0,
            116.0,
            image=self.logo_img
        )

        # Contact Illustration
        self.illus_img = PhotoImage(
            file=self.relative_to_assets("contact_illus.png"))
        self.contact_illus = self.canvas.create_image(
            725.0,
            387.0,
            image=self.illus_img
        )

        # "facebook" ICON
        self.fb_img = PhotoImage(
            file=self.relative_to_assets("icon__fb.png"))
        self.fb_btn = Button(
            image=self.fb_img,
            borderwidth=0,
            background="#fff",
            highlightthickness=0,
            command=self.handle_fb,
            relief="flat"
        )
        self.fb_btn.place(
            x=85.0,
            y=533.0,
            width=28.0,
            height=28.0
        )

        # "in" ICON
        self.in_img = PhotoImage(
            file=self.relative_to_assets("icon__in.png"))
        self.in_btn = Button(
            image=self.in_img,
            borderwidth=0,
            background="#fff",
            highlightthickness=0,
            command=self.handle_in,
            relief="flat"
        )
        self.in_btn.place(
            x=133.0,
            y=533.0,
            width=28.0,
            height=28.0
        )

        # "mail" ICON
        self.mail_img = PhotoImage(
            file=self.relative_to_assets("icon__mail.png"))
        self.mail_btn = Button(
            image=self.mail_img,
            borderwidth=0,
            background="#fff",
            highlightthickness=0,
            command=self.handle_mail,
            relief="flat"
        )
        self.mail_btn.place(
            x=182.0,
            y=533.0,
            width=28.0,
            height=28.0
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

    def handle_backhome(self):
        print()
    
    def handle_fb(self):
        print()
    
    def handle_in(self):
        print()
    
    def handle_mail(self):
        print()
    
    def handle_exit(self):
        self.window.destroy()
    
    def handle_form(self):
        print()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)
    

if __name__ == '__main__':
    window = Tk()
    menu = ContactGUI(window)
    window.resizable(False, False)
    window.mainloop()