
from pathlib import Path
import webbrowser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import gui_solver
import gui_contact
import gui_about
import gui_how2use

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

class MenuGUI:
    def __init__(self, window) -> None:
        # Handle assets file path
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path(r"../assets")

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

        # "Exit" BUTTON
        self.exit_img = PhotoImage(
            file=self.relative_to_assets("btn__exit.png"))
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
    
    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)
    
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
    
    def handle_exit(self):
        self.window.destroy()
    
    def handle_fb(self):
        webbrowser.open("https://facebook.com/")
    
    def handle_in(self):
        webbrowser.open("https://linkedin.com/")
    
    def handle_mail(self):
        receiver_email = "truong.pd214937@sis.hust.edu.vn; quy.dnc214927@sis.hust.edu.vn; truc.nt214936@sis.hust.edu.vn;"
        subject = "[HELAX] Enter your title..."

        body = "### Enter your message..."

        message = MIMEMultipart()
        message["From"] = "truong.pd214937@sis.hust.edu.vn; quy.dnc214927@sis.hust.edu.vn; truc.nt214936@sis.hust.edu.vn;"
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        webbrowser.open(f"mailto:{receiver_email}?subject={subject}&body={body}")


if __name__ == '__main__':
    window = Tk()
    menu = MenuGUI(window)
    window.resizable(False, False)
    window.mainloop()
