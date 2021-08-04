import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdfac"
BUTTON_TEXT_COLOR = "#000000"
BUTTON_BG_COLOR = "#ffffff"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_TITLE = (FONT_NAME, 35,"bold")
FONT_NORMAL = (FONT_NAME, 15,"bold")
CHECK = "✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    window.after_cancel(timer)
    reps = 0
    title.config(text="T I M E R",fg=GREEN)
    pomodoros.config(text="---")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_work():
    global timer
    if timer is not None:
        reset()
    pomodoros.config(text="")
    intern_mechanism()

def intern_mechanism():
    global reps
    reps+=1

    if reps == 8:  #reps = 8
        minutes = LONG_BREAK_MIN
        reps = 0
        title.config(text="B R E A K",fg=RED)

    elif reps % 2==0: #reps = 2,4,6
        minutes = SHORT_BREAK_MIN
        title.config(text="B R E A K",fg=PINK)
    else:             #reps = 1,3,5,7
        minutes = WORK_MIN
        title.config(text=" W O R K ",fg=GREEN)

    count_down(minutes*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count/60) #aprox down
    count_second = count % 60 #remaind

    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")

    if count >= 0:
        timer = window.after(1000,count_down,count-1)
    else:
        intern_mechanism()
        if reps % 2 == 0:
            pomodoros.config(text=f"{pomodoros['text']}{CHECK}")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)#the first two values are the center of the Canva
canvas.grid(row=1,column=0,columnspan=3)

timer_text = canvas.create_text(100,132,text="00:00",fill="black", font=FONT_TITLE)

title = tkinter.Label()
title.config(text="T I M E R", foreground=GREEN, bg=YELLOW, font=FONT_TITLE)
title.grid(row=0,column=0,columnspan=3)

start_button= tkinter.Button(command=start_work)
start_button.config(text="Start", bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
start_button.grid(row=2,column=0)

reset_button = tkinter.Button(command=reset)
reset_button.config(text="Reset", bg=BUTTON_BG_COLOR, fg=BUTTON_TEXT_COLOR)
reset_button.grid(row=2,column=2)

pomodoros = tkinter.Label()
pomodoros.config(text="---", fg=GREEN, bg=YELLOW, font=FONT_NORMAL)
pomodoros.grid(row=2,column=1)


window.mainloop()

