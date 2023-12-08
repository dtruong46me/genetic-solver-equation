import os
import sys

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class ResultGUI:
    def __init__(self, window, input_data="", output_data="", exc_time="", x_results=[], y_results=[]) -> None:
        # Handle assets file path
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path(r"../assets")

        self.x_results = x_results
        self.y_results = y_results

        self.window = window
        self.input_data = input_data
        self.output_data = output_data

        self.window.geometry("1000x600")
        self.window.configure(bg="#FFF")
        self.window.title("Genetic Solver Equation")

        self.icon_path = PhotoImage(file=self.relative_to_assets("helax__x.png"))
        self.window.iconphoto(True, self.icon_path)

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

        # "Advance" BUTTON
        self.advance_img = PhotoImage(
            file=self.relative_to_assets("btn__advance_mode.png"))
        self.advance_btn = Button(
            image=self.advance_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_advance,
            relief="flat"
        )
        self.advance_btn.place(
            x=810.0,
            y=36.0,
            width=117.0,
            height=42.0
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
        if len(self.input_data) <= 50:
            self.canvas.create_text(
                279.0,
                286.0,
                anchor="nw",
                text=self.input_data,
                fill="#031F4B",
                font=("Consolas Bold", 16 * -1)
            )
        
        if len(self.input_data) > 50 and len(self.input_data) <= 67:
            self.canvas.create_text(
                269.0,
                290.0,
                anchor="nw",
                text=self.input_data,
                fill="#031F4B",
                font=("Consolas Bold", 12 * -1)
            )
        
        if len(self.input_data) > 67:
            self.canvas.create_text(
                269.0,
                290.0,
                anchor="nw",
                text=self.input_data[:65] + "..",
                fill="#031F4B",
                font=("Consolas Bold", 12 * -1)
            )

        # Output
        self.canvas.create_text(
            279.0,
            363.0,
            anchor="nw",
            text=self.output_data,
            fill="#031F4B",
            font=("Consolas Bold", 16 * -1)
        )

        # Time
        self.canvas.create_text(
            279.0,
            440.0,
            anchor="nw",
            text=exc_time,
            fill="#031F4B",
            font=("Consolas Bold", 16 * -1)
        )

        # "Exit" BUTTON
        self.exit_big_img = PhotoImage(
            file=self.relative_to_assets("btn__exit_big.png"))
        self.exit_big_btn = Button(
            image=self.exit_big_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_exit,
            relief="flat"
        )
        self.exit_big_btn.place(
            x=290.5,
            y=506.0,
            width=123.0,
            height=47.0
        )

        # "Visualize" BUTTON
        self.viz_img = PhotoImage(
            file=self.relative_to_assets("btn__visualize.png"))
        self.viz_btn = Button(
            image=self.viz_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_visualize,
            relief="flat"
        )
        self.viz_btn.place(
            x=586.5,
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
            x=438.5,
            y=506.0,
            width=123.0,
            height=47.0
        )

        self.continue_btn.bind("<Return>", lambda event: self.handle_continue())
        self.continue_btn.focus_set()
    
    def handle_backhome(self):
        self.current_gui = None
        for widget in self.window.winfo_children():
            widget.destroy()

        from gui_menu import MenuGUI
        self.backhome_gui = MenuGUI(self.window)
        self.current_gui = self.backhome_gui

    def handle_advance(self):
        self.current_gui = None
        for widget in self.window.winfo_children():
            widget.destroy()

        from advance_solver import AdvanceSolverGUI
        self.backhome_gui = AdvanceSolverGUI(self.window)
        self.current_gui = self.backhome_gui

    def handle_exit(self):
        self.window.destroy()

    def handle_visualize(self):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        sys.path.insert(0, path)
        from object.visualize import Visualize
        if self.input_data != "":
            visualizer = Visualize()
            visualizer.plot_result(self.x_results, self.y_results)

        self.current_gui = None
        for widget in self.window.winfo_children():
            widget.destroy()

        from gui_visualize import VisualizeGUI
        self.visualize_gui = VisualizeGUI(self.window, self.input_data, self.output_data)
        self.current_gui = self.visualize_gui
    
    def handle_continue(self):
        self.current_gui = None
        for widget in self.window.winfo_children():
            widget.destroy()

        from gui_solver import SolverGUI
        self.solver_gui = SolverGUI(self.window)
        self.current_gui = self.solver_gui

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)
    

if __name__ == '__main__':
    window = Tk()
    menu = ResultGUI(window)
    window.resizable(False, False)
    window.mainloop()