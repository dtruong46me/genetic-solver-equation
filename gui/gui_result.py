

from pathlib import Path
import gui_menu
import gui_solver

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class ResultGUI:
    def __init__(self, window, input_data=None) -> None:
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

        # Result Frame
        self.result_frame_img = PhotoImage(
            file=self.relative_to_assets("result_frame.png"))
        self.result_frame = self.canvas.create_image(
            499.0,
            355.0,
            image=self.result_frame_img
        )

        # Input
        self.canvas.create_text(
            279.0,
            286.0,
            anchor="nw",
            text=input_data,
            fill="#031F4B",
            font=("Consolas Bold", 16 * -1)
        )

        # Output
        self.canvas.create_text(
            279.0,
            363.0,
            anchor="nw",
            text="x=0.0000000001",
            fill="#031F4B",
            font=("Consolas Bold", 16 * -1)
        )

        # Time
        self.canvas.create_text(
            279.0,
            440.0,
            anchor="nw",
            text="0.00423ms",
            fill="#031F4B",
            font=("Consolas Bold", 16 * -1)
        )

        # "Exit" BUTTON
        self.exit_img = PhotoImage(
            file=self.relative_to_assets("btn__exit_big.png"))
        self.exit_btn = Button(
            image=self.exit_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_exit,
            relief="flat"
        )
        self.exit_btn.place(
            x=364.0,
            y=506.0,
            width=123.0,
            height=47.0
        )

        # "Continue" BUTTON
        self.continue_img = PhotoImage(
            file=self.relative_to_assets("btn__continue.png"))
        self.continue_btn = Button(
            image=self.continue_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_continue,
            relief="flat"
        )
        self.continue_btn.place(
            x=513.0,
            y=506.0,
            width=123.0,
            height=47.0
        )
    
    def handle_backhome(self):
        self.current_gui = None
        for widget in self.window.winfo_children():
            widget.destroy()

        self.backhome_gui = gui_menu.MenuGUI(self.window)
        self.current_gui = self.backhome_gui

    def handle_setting(self):
        print()

    def handle_exit(self):
        self.window.destroy()
    
    def handle_continue(self):
        self.current_gui = None
        for widget in self.window.winfo_children():
            widget.destroy()

        self.solver_gui = gui_solver.SolverGUI(self.window)
        self.current_gui = self.solver_gui

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)
    

if __name__ == '__main__':
    window = Tk()
    menu = ResultGUI(window)
    window.resizable(False, False)
    window.mainloop()