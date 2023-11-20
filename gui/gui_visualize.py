

from pathlib import Path
import gui_menu
import gui_solver

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class VisualizeGUI:
    def __init__(self, window, input_data="", output_data="") -> None:
        # Handle assets file path
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path(r"../assets")
        self.vizs_path = self.output_path / Path(r"../assets/viz")

        self.window = window

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
            500.0,
            88.0,
            image=self.logo_img
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

        # Input
        self.input_frame_png = PhotoImage(
            file=self.relative_to_assets("frame_input.png"))
        self.input_frm = self.canvas.create_image(
            378.0,
            152.0,
            image=self.input_frame_png
        )

        if len(input_data) <= 50:
            self.canvas.create_text(
                162.0,
                146.0,
                anchor="nw",
                text=input_data,
                fill="#6497B1",
                font=("Consolas Bold", 16 * -1)
            )
        
        if len(input_data) > 50:
            self.canvas.create_text(
                162.0,
                146.0,
                anchor="nw",
                text=input_data[:-2] + "..",
                fill="#6497B1",
                font=("Consolas Bold", 16 * -1)
            )

        # Output
        self.output_frame_png = PhotoImage(
            file=self.relative_to_assets("frame_output.png"))
        self.output_frm = self.canvas.create_image(
            744.0,
            152.0,
            image=self.output_frame_png
        )

        if len(output_data) <= 17:
            self.canvas.create_text(
                666.0,
                146.0,
                anchor="nw",
                text=output_data[:-2] + "..",
                fill="#6497B1",
                font=("Consolas Bold", 16 * -1)
            )
        
        if len(output_data) > 17:
            self.canvas.create_text(
                666.0,
                146.0,
                anchor="nw",
                text=output_data[:-2] + "..",
                fill="#6497B1",
                font=("Consolas Bold", 16 * -1)
            )

        # x_value frame
        self.x_value_png = PhotoImage(
            file=self.relative_to_assets("frame_viz.png"))
        self.x_value_frame = self.canvas.create_image(
            297.0,
            341.0,
            image=self.x_value_png
        )

        self.x_viz_img = PhotoImage(file=self.relative_to_viz("x.png"))
        self.x_viz = self.canvas.create_image(
            297.0,
            341.0,
            image=self.x_viz_img
        )

        # y_value frame
        self.y_value_png = PhotoImage(
            file=self.relative_to_assets("frame_viz.png"))
        self.y_value_frame = self.canvas.create_image(
            702.0,
            341.0,
            image=self.y_value_png
        )

        self.y_viz_img = PhotoImage(file=self.relative_to_viz("y.png"))
        self.y_viz = self.canvas.create_image(
            702.0,
            341.0,
            image=self.y_viz_img
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

        self.continue_btn.bind("<Return>", lambda event: self.handle_continue())
        self.continue_btn.focus_set()
    
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
    
    def relative_to_viz(self, path: str) -> Path:
        return self.vizs_path / Path(path)
    

if __name__ == '__main__':
    window = Tk()
    menu = VisualizeGUI(window)
    window.resizable(False, False)
    window.mainloop()