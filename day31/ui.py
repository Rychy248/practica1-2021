import tkinter
import time
from tkinter import messagebox

import dataManager

# ---------------------------- UI SETUP ------------------------------- #
PINK = "#e2979c"
RED = "#555544" #"#e7305b"
GREEN = "#3d550c"
YELLOW = "#f7f5dd"
BT_TX_COLOR = "#000000"
BG_GEN_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
FONT_TITLE = (FONT_NAME, 25,"bold")
FONT_NORMAL = (FONT_NAME, 15,"bold")

class UI():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Flashy")
        self.window.config(padx=50, pady=50, bg=BG_GEN_COLOR)
        self.data = dataManager.DataManager()
        
        self.my_vars()
        self.canvas()
        self.labels()
        self.buttons()
        self.know()
        self.window.mainloop()

    def canvas(self):
        self.card_front = tkinter.PhotoImage(file="images/card_front.png")
        self.card_back = tkinter.PhotoImage(file="images/card_back.png")

        self.canvas = tkinter.Canvas(width=800, height=526, bg=BG_GEN_COLOR, highlightthickness=0)
        self.card_img = self.canvas.create_image(400, 263, image=self.card_front)
        self.card_languague = self.canvas.create_text(400,150, text="Title",font=("Ariel",40,"italic"))
        self.card_word = self.canvas.create_text(400,263, text="Word",font=("Ariel",60,"bold"))
        self.canvas.grid(row=1,column=0, columnspan=2)

    def unknow(self):
        self.window.after_cancel(self.flag_time)
        try:
            if self.unknow_word:
                self.canvas.itemconfig(self.card_img, image=self.card_back)
                self.canvas.itemconfig(self.card_languague, text="Sphanish", fill="white")
                self.canvas.itemconfig(self.card_word, text=f"{self.sphanish}", fill="white")
                self.unknow_word = False
            else:
                self.canvas.itemconfig(self.card_img, image=self.card_front)
                self.canvas.itemconfig(self.card_languague, text="English", fill="black")
                self.canvas.itemconfig(self.card_word, text=f"{self.english}", fill="black")
                self.unknow_word = True
        except AttributeError:
            self.canvas.itemconfig(self.card_img, image=self.card_front)
            self.know()

        self.flag_time = self.window.after(3000,func=self.unknow)
    
    def know(self):
        self.window.after_cancel(self.flag_time)
        if not self.unknow_word:
            self.canvas.itemconfig(self.card_img, image=self.card_front)
            self.unknow_word=True

        if self.english is not None:
            self.data.delete_unknow_words(self.english)

        word = self.data.nex_word()
        self.english = str(word[0])
        self.sphanish = str(word[1])
        self.canvas.itemconfig(self.card_languague, text="English", fill="black")
        self.canvas.itemconfig(self.card_word, text=f"{self.english}", fill="black")

        self.flag_time = self.window.after(3000,func=self.unknow)

    def my_vars(self):
        self.unknow_word = False
        self.english = None
        self.sphanish = None
        self.flag_time = self.window.after(3000,func=self.unknow)

    def labels(self):
        self.title = tkinter.Label()
        self.title.config(text=" H I - T H E R E - :) Learning english!", foreground=RED, bg=BG_GEN_COLOR, font=FONT_TITLE)
        self.title.grid(row=0,column=0,columnspan=2)


    def buttons(self):
        self.unknow_image = tkinter.PhotoImage(file="images/wrong.png")
        self.btt_unknow = tkinter.Button(command=self.unknow)
        self.btt_unknow.config(bg=BG_GEN_COLOR, highlightthickness=0)
        self.btt_unknow.config(image=self.unknow_image)
        self.btt_unknow.grid(row=2,column=0)

        self.know_image = tkinter.PhotoImage(file="images/right.png")
        self.btt_know = tkinter.Button(command=self.know) 
        self.btt_know.config(bg=BG_GEN_COLOR, highlightthickness=0)
        self.btt_know.config(image=self.know_image)
        self.btt_know.grid(row=2,column=1)

