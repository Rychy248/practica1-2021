import random
import tkinter
import pyclip #need pip install pyclip
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
class RandomPassword():
    def __init__(self):
        self.SIGNS = ['#','!','?','@','=','-','*','_','&','/','%']
        self.LETTERS = ['A','B''C','D','E','F','G','H','I','J','K','L','M','N','O',
                   'P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d',
                   'e','f','g','h','i','j','k','l','o','p','q','r','s','t','u',
                   'v','w','x','y','z']
        self.NUMBERS = [f"{n}" for n in range(1,11)] # 1-10

    def get(self):
        letters = [random.choice(self.LETTERS) for _ in range(random.randint(1,4))]
        numbers = [random.choice(self.NUMBERS) for _ in range(random.randint(1,4))]
        signs = [random.choice(self.SIGNS) for _ in range(random.randint(1,4))]
        chars = letters + numbers + signs

        random.shuffle(chars)
        password = "".join(chars) #joing return a string with the
        #elements from an iterable separated by the strign passed
        return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
class AdminPass():
    all_passwords = None

    def red_pass(self):
        with open("passwords.csv") as file:
            all_passwords = file.readlines()

    def save(self,web, mail_user, password):
        csv = f"\n{web},{mail_user},{password}"
        with open("passwords.csv","a") as file:
            file.write(csv)


# ---------------------------- UI SETUP ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#3d550c"
YELLOW = "#f7f5dd"
BT_TX_COLOR = "#000000"
BG_GEN_COLOR = "#ffffff"
FONT_NAME = "Courier"
FONT_TITLE = (FONT_NAME, 35,"bold")
FONT_NORMAL = (FONT_NAME, 15,"bold")

#-----class instance
rand_pass = RandomPassword()
admin_pass = AdminPass()
#-----
def save_pass():
    if len(web_var.get()) == 0 or len(mail_var.get()) == 0 or len(pass_var.get()) == 0:
        if len(web_var.get()) == 0:
            messagebox.showinfo(title="Something empty",message="Oops, the Web field is emty!")
        elif len(mail_var.get()) == 0:
            messagebox.showinfo(title="Something empty",message="Oops, Email/User field is emty!")
        else:
            messagebox.showinfo(title="Something empty",message="Oops, Password field is emty!")
    else:
        message = f"These are the details\nWeb: {web_var.get()}\nEmail/Username:"\
                  f"{mail_var.get()}\nPassword: {pass_var.get()}\n\nIs it okay to save?"
        is_okay = messagebox.askokcancel(title=f"{web_var.get()}",message=message)
        if is_okay:
            admin_pass.save(web_var.get(),mail_var.get(),pass_var.get())
            web_var.set("")
            mail_var.set("")
            pass_var.set("")
            messagebox.showinfo(title="Saved",message="Credentials Saved")

def generate_pass():
    global first_time_program
    pass_var.set(rand_pass.get())
    pyclip.copy(pass_var.get())
    if first_time_program:
        messagebox.showinfo(title="Password copy",message="Your Password it's in your Clipboard")
        first_time_program = False

first_time_program = True

window = tkinter.Tk()
window.title("PASSWORD MANAGER")
window.config(padx=20, pady=20, bg=BG_GEN_COLOR)

title = tkinter.Label()
title.config(text="P A S S O W R D L A N D", foreground=RED, bg=BG_GEN_COLOR, font=FONT_TITLE)
title.grid(row=0,column=0,columnspan=4)

canvas = tkinter.Canvas(width=200, height=224, bg=BG_GEN_COLOR, highlightthickness=0)
key_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_img)
canvas.grid(row=1,column=0,columnspan=4)

#Labels
website= tkinter.Label()
website.config(width=15, text="Website", fg=GREEN, bg=BG_GEN_COLOR, font=FONT_NORMAL)
website.grid(row=2,column=0)
user_mail= tkinter.Label()
user_mail.config(width=15, text="Email/Username", fg=GREEN, bg=BG_GEN_COLOR, font=FONT_NORMAL)
user_mail.grid(row=3,column=0)
password= tkinter.Label()
password.config(width=15, text="Password", fg=GREEN, bg=BG_GEN_COLOR, font=FONT_NORMAL)
password.grid(row=4,column=0)

#variables
web_var = tkinter.StringVar()
mail_var = tkinter.StringVar()
pass_var = tkinter.StringVar()

#Entrys
web_entry = tkinter.Entry()
web_entry.config(width=35, textvariable=web_var, font=FONT_NORMAL)
web_entry.focus()
web_entry.grid(row=2,column=1,columnspan=3)
mail_entry = tkinter.Entry()
mail_entry.config(width=35, textvariable=mail_var, font=FONT_NORMAL)
mail_entry.insert('end',"example@gmail.com")
mail_entry.grid(row=3,column=1,columnspan=3)
pass_entry = tkinter.Entry()
pass_entry.config(width=21, textvariable=pass_var, font=FONT_NORMAL)
pass_entry.grid(row=4,column=1)

#timer_text = canvas.create_text(100,132,text="00:00",fill="black", font=FONT_TITLE)
#Buttons
btt_get_pass = tkinter.Button(command=generate_pass)
btt_get_pass.config(width=12, text="Generate Password", bg=BG_GEN_COLOR, fg=BT_TX_COLOR)
btt_get_pass.grid(row=4,column=3)

btt_add = tkinter.Button(command=save_pass)
btt_add.config(width=50, text="Add", bg=BG_GEN_COLOR, fg=BT_TX_COLOR)
btt_add.grid(row=6,column=1,columnspan=3)

window.mainloop()
