
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class SolverGUI:
    def __init__(self, window) -> None:
        # Handle assets file path
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path(r"../assets")

        self.window = window

        self.window.geometry("1000x600")
        self.window.configure(bg="#FFF")

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

        # HelaX LOGO
        self.logo_img = PhotoImage(
            file=self.relative_to_assets("helax__logo.png"))
        self.helax_logo = self.canvas.create_image(
            501.0,
            126.0,
            image=self.logo_img
        )

        # Genetic Solver Equation
        self.gse_img = PhotoImage(
            file=self.relative_to_assets("gse__name.png"))
        self.gse_text = self.canvas.create_image(
            499.0,
            187.0,
            image=self.gse_img
        )

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

        # "Setting" BUTTON
        self.setting_img = PhotoImage(
            file=self.relative_to_assets("btn__setting.png"))
        self.setting_btn = Button(
            image=self.setting_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_setting,
            relief="flat"
        )
        self.setting_btn.place(
            x=820.0,
            y=15.0,
            width=125.0,
            height=52.0
        )

        # Entry input background
        self.entry_img = PhotoImage(
            file=self.relative_to_assets("entry.png"))
        self.entry_bg = self.canvas.create_image(
            499.5,
            273.5,
            image=self.entry_img
        )

        # Entry input
        self.entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#031F4B",
            highlightthickness=0,
            font=("Consolas", 16),
        )
        self.entry.place(
            x=215.0,
            y=248.0,
            width=571.0,
            height=52.0
        )

        # "Submit" BUTTON
        self.submit_img = PhotoImage(
            file=self.relative_to_assets("btn__submit.png"))
        self.submit_btn = Button(
            image=self.submit_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_submit,
            relief="flat"
        )
        self.submit_btn.place(
            x=426.0,
            y=335.0,
            width=147.0,
            height=56.0
        )

        self.quote_img = PhotoImage(
            file=self.relative_to_assets("quote.png"))
        self.quote = self.canvas.create_image(
            499.0,
            517.0,
            image=self.quote_img
        )

    def handle_submit(self):
        print()
    
    def handle_backhome(self):
        print()

    def handle_setting(self):
        print()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)
    

if __name__ == '__main__':
    window = Tk()
    menu = SolverGUI(window)
    window.resizable(False, False)
    window.mainloop()