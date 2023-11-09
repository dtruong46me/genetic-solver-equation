
from pathlib import Path
import gui_menu
import webbrowser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class AboutGUI:
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

        # About Illustration
        self.illus_img = PhotoImage(
            file=self.relative_to_assets("about_illus.png"))
        self.about_illus = self.canvas.create_image(
            280.0,
            322.0,
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
        self.current_gui = None
        for widget in self.window.winfo_children():
            widget.destroy()

        self.backhome_gui = gui_menu.MenuGUI(self.window)
        self.current_gui = self.backhome_gui
    
    def handle_fb(self):
        webbrowser.open("https://www.facebook.com/")
    
    def handle_in(self):
        webbrowser.open("https://www.linkedin.com/")
    
    def handle_mail(self):
        receiver_email = "dtruong46.me@example.com"
        subject = "[HELAX] Enter your title..."

        body = "### Enter your message..."

        message = MIMEMultipart()
        message["From"] = "dtruong46.me@example.com"
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        webbrowser.open(f"mailto:{receiver_email}?subject={subject}&body={body}")
    
    def handle_exit(self):
        self.window.destroy()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)
    

if __name__ == '__main__':
    window = Tk()
    menu = AboutGUI(window)
    window.resizable(False, False)
    window.mainloop()