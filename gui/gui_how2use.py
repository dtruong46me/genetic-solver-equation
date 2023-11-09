
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class How2UseGUI:
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

        # How2Use Illustration
        self.illus_img = PhotoImage(
            file=self.relative_to_assets("how2use_illus.png"))
        self.how2use_illus = self.canvas.create_image(
            258.0,
            355.0,
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
            command=self.handle_startnow,
            relief="flat"
        )
        self.inhere_btn.place(
            x=536.0,
            y=348.0,
            width=52.0,
            height=19.0
        )

        # "Start now" BUTTON
        self.exit_img = PhotoImage(
            file=self.relative_to_assets("btn__startnow.png"))
        self.exit_btn = Button(
            image=self.exit_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_startnow,
            relief="flat"
        )
        self.exit_btn.place(
            x=778.0,
            y=524.0,
            width=142.0,
            height=46.0
        )

    def handle_backhome(self):
        print()
    
    def handle_fb(self):
        print()
    
    def handle_in(self):
        print()
    
    def handle_mail(self):
        print()
    
    def handle_startnow(self):
        print()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)
    

if __name__ == '__main__':
    window = Tk()
    menu = How2UseGUI(window)
    window.resizable(False, False)
    window.mainloop()