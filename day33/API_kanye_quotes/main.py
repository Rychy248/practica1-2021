from tkinter import *
import requests

# API endpoint Kanye quotes https://api.kanye.rest/
# web https://kanye.rest/

def get_quote(recursion_flag=1):
    try:
        response = requests.get(url="https://api.kanye.rest/")
        data = response.json()

        font_size=30
        if len(data['quote']) < 90:
            font_size=25
        elif len(data['quote']) < 120:
            font_size=20
        elif len(data['quote']) < 150:
            font_size=15
        else:
            font_size=10

        canvas.itemconfig(
            quote_text,
            text=f"{data['quote']}",
            font=("Arial", font_size, "bold")
            )
    except Exception as e:
        print(f"An error has ocurred {e}\n")
        if recursion_flag <= 3:
            print(f"\nTrygin... {recursion_flag}")
            get_quote(recursion_flag+1)
        else:
            print("Recursive error, API not answer")

def ui():
    global canvas, quote_text
    window = Tk()
    window.title("Kanye Says...")
    window.config(padx=50, pady=50, bg="white")

    canvas = Canvas(width=300, height=414, bg="white", highlightthickness=0)
    background_img = PhotoImage(file="background.png")
    canvas.create_image(150, 207, image=background_img)
    quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="black")
    canvas.grid(row=0, column=0)
    
    get_quote()
    kanye_img = PhotoImage(file="kanye.png")
    kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote,bg="white")
    kanye_button.grid(row=1, column=0)
    window.mainloop()

ui()