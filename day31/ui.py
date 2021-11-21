import tkinter
from tkinter import messagebox

# ---------------------------- UI SETUP ------------------------------- #
PINK = "#e2979c"
RED = "#555544" #"#e7305b"
GREEN = "#3d550c"
YELLOW = "#f7f5dd"
BT_TX_COLOR = "#000000"
BG_GEN_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
FONT_TITLE = (FONT_NAME, 35,"bold")
FONT_NORMAL = (FONT_NAME, 15,"bold")


#-----
def save_pass():
    website = (web_var.get()).title()
    mail = mail_var.get()
    pass_user = pass_var.get()

    message = f"These are the details\nWeb: {web_var.get()}\nEmail/Username:"\
              f"{mail_var.get()}\nPassword: {pass_var.get()}\n\nIs it okay to save?"
    is_okay = messagebox.askokcancel(title=f"{web_var.get()}",message=message)
    if is_okay:
        admin_pass.save(website,mail,pass_user)
        web_var.set("")
        mail_var.set("")
        pass_var.set("")
        messagebox.showinfo(title="Saved",message="Credentials Saved")

def search_web():
    website = web_var.get()
    admin_pass.search(website)

def generate_pass():
    global first_time_program
    pass_var.set(rand_pass.get())
    pyclip.copy(pass_var.get())
    if first_time_program:
        messagebox.showinfo(title="Password copy",message="Your Password it's in your Clipboard")
        first_time_program = False

first_time_program = True
class UI():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Flashy")
        self.window.config(padx=50, pady=50, bg=BG_GEN_COLOR)

        self.title = tkinter.Label()
        self.title.config(text=" H I - T H E R E - :)\nLearnign english!", foreground=RED, bg=BG_GEN_COLOR, font=FONT_TITLE)
        self.title.grid(row=0,column=0)
        self.canvas()
        #self.labels()
        #self.my_vars()
        #self.entrys()
        self.buttons()
        self.window.mainloop()

    def canvas(self):
        #self.canvas = tkinter.Canvas(width=800, height=526, bg=BG_GEN_COLOR, highlightthickness=0)
        self.card_img = tkinter.PhotoImage(file="images/card_front.png")
        self.canvas = tkinter.Canvas(width=800, height=526, bg=BG_GEN_COLOR, highlightthickness=0)
        self.canvas.create_image(400, 263, image=self.card_img)
        self.canvas.create_text(400,150, text="Title",font=("Ariel",40,"italic"))
        self.canvas.create_text(400,263, text="Title",font=("Ariel",60,"bold"))
        self.canvas.grid(row=1,column=0)

    def labels(self):
        self.website= tkinter.Label()
        self.website.config(width=15, text="Website", fg=GREEN, bg=BG_GEN_COLOR, font=FONT_NORMAL)
        self.website.grid(row=2,column=0)


    def my_vars(self):
        #variables
        self.web_var = tkinter.StringVar()
        self.mail_var = tkinter.StringVar()
        self.pass_var = tkinter.StringVar()

    def entrys(self):
        #Entrys
        self.web_entry = tkinter.Entry()
        self.web_entry.config(width=21, textvariable=self.web_var, font=FONT_NORMAL)
        self.web_entry.focus()
        self.web_entry.grid(row=2,column=1)
        self.mail_entry = tkinter.Entry()
        self.mail_entry.config(width=35, textvariable=self.mail_var, font=FONT_NORMAL)
        self.mail_entry.insert('end',"example@gmail.com")
        self.mail_entry.grid(row=3,column=1,columnspan=3)
        self.pass_entry = tkinter.Entry()
        self.pass_entry.config(width=21, textvariable=self.pass_var, font=FONT_NORMAL)
        self.pass_entry.grid(row=4,column=1)

    def buttons(self):
        #timer_text = canvas.create_text(100,132,text="00:00",fill="black", font=FONT_TITLE)
        #Buttons
        
        x_image = tkinter.PhotoImage(file="images/wrong.png")
        self.btt_unknow= tkinter.Button(command=search_web)
        self.btt_unknow.config(width=12, text="Search", bg=BG_GEN_COLOR, fg=BT_TX_COLOR)
        self.btt_unknow.config(image=x_image)
        self.btt_unknow.grid(row=2,column=2)

        know_image = tkinter.PhotoImage(file="images/right.png")
        self.btt_know = tkinter.Button(command=generate_pass)
        self.btt_know.config(width=12, text="Generate Password", bg=BG_GEN_COLOR, fg=BT_TX_COLOR)
        self.btt_know.config(image=know_image)
        self.btt_know.grid(row=2,column=2)

