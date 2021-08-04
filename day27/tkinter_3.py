import tkinter

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

def button2_hi():
    my_label.config(text="HI! ATT:New Button")
window = tkinter.Tk()
window.title("My Third GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)
#if we add the padding into a window, this padding will be seting into all of our widths

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button",command=button2_hi)
new_button.grid(column=2, row=0)

#Entry
input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=1, row=2)





window.mainloop()
