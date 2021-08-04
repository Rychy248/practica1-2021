#Pack Documentation = http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
#Tkinter Documentation = https://docs.python.org/3/library/tkinter.html#the-packer

import tkinter
def button_clicked():
    my_label["text"] = f"Hou, you clicked me! :)\n an you typed = {my_input.get()}"

window = tkinter.Tk()
window.title("My First GUI whit Tkinter")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I'm a Label", font=("Arial",24,"bold"))
my_label["text"] = "Hi there!"
my_label.config(text = f"{my_label['text']} + New text")
my_label.pack()

#Button
button = tkinter.Button(text="Click me",command=button_clicked)
button.pack()

#Entry
my_input = tkinter.Entry(width=10)
my_input.pack()

"""
window.mainloop() #is equivalent to
while True:
    window_listenig()
"""
window.mainloop()
