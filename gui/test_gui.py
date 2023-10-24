import tkinter as tk
from PIL import ImageTk, Image

class GeneticSolverEquationApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Genetic Solver Equation")
        self.root.geometry("900x600")

        self.bg = ImageTk.PhotoImage(Image.open("imgs/background.png"))
        self.bglabel = tk.Label(self.root, image=self.bg)
        self.bglabel.place(relheight=1, relwidth=1)

        self.label = tk.Label(self.root, text="Genetic Solver Equation", font=("Roboto", 16))
        self.label.pack()

        self.logo = ImageTk.PhotoImage(Image.open("imgs/logo.png"))
        self.logo_label = tk.Label(self.root, image=self.logo)
        self.logo_label.pack()
        
        self.input = tk.Entry(self.root, font=("Roboto", 12))
        self.input.insert(index=2, string="Enter your equation...")
        self.input.pack(pady=10)

        self.input.bind("<FocusIn>", self.on_entry_focus_in)
        self.input.bind("<FocusOut>", self.on_entry_focus_out)

        self.solve = tk.Button(self.root, text="SOLVE", font=("Roboto", 14), command=self.solve_equation)
        self.solve.pack()

    def solve_equation():

        pass

    def on_entry_focus_in(self, event):
        if self.input.get() == "Enter your equation...":
            self.input.delete(0, "end")

    def on_entry_focus_out(self, event):
        if not self.input.get():
            self.input.insert(0, "Enter your equaiton...")

if __name__ == '__main__':
    gseapp = GeneticSolverEquationApp()
    gseapp.root.mainloop()