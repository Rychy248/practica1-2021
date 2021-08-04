import tkinter

TITLE = ("Arial",25,"bold")
FONT = ("Arial",15,"bold")
RESULT = ("Arial",20,"bold")

def convert():
    var_miles = float(entry_miles.get())
    kilometers["text"] = f"Result: {var_miles*1.6}"

#Window 
window = tkinter.Tk()
window.title("Mile to Kilometers")
window.minsize(width=500, height=300)
window.config(padx=10, pady=20)

#Label
title = tkinter.Label(text="M I L E - T O - K I L O M E T E R S",font=TITLE)
title.grid(row=0, column=0, columnspan=2)

miles = tkinter.Label(text="Entry miles: ",font=FONT)
miles.grid(row=1, column=0)

kilometers = tkinter.Label(text="Result: ",font=RESULT)
kilometers.grid(row=3,column=0)

#Entry
entry_miles = tkinter.Entry()
entry_miles.grid(row=1, column=1)

#Button
button = tkinter.Button(text="Convert",font=FONT, command=convert)
button.grid(row=2, column=0, columnspan=2)


window.mainloop()
