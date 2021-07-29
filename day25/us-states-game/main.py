from turtle import Turtle, Screen
from writer import Writer, Progress
from data import PandaData

IMAGE = "blank_states_img.gif"

def split_word(text):
    """Similar to 'title()' method, but in this funtion, we delete all especes in the start and end
    or between two words"""
    words = text.rsplit(" ")
    output_text = ""

    index = 0
    for word in words:
        output_text += (word.strip()).capitalize() + " "
        index += 0

    output_text = output_text.rstrip(" ")
    output_text = output_text.lstrip(" ")

    return output_text

screen = Screen()
screen.title("US States Game")
screen.addshape(IMAGE)
screen.colormode(255)
turtle = Turtle()
turtle.shape(IMAGE)
write = Writer()
progress = Progress()
data = PandaData()
messegue = "Guess a State"
right_answers = 0
guesed_states = []

for oportunity in range(50):
    messegue = f"Right Answers: {right_answers}/50 - intents: {oportunity} of 50"
    progress.update_progress(messegue)
    answer = screen.textinput(title="Guess a State",prompt="What's the next state's name? ")
    answer = split_word(answer)
    if answer == "Exit":
        break
    elif data.find_a_state(answer):
        if answer not in guesed_states:
            guesed_states.append(answer)
            coor = data.get_coor_state(answer)
            write.write_name(answer,coor)
            right_answers += 1
messegue = f"Right Answers: {right_answers}/50 - intents: 50 of 50"
progress.update_progress(messegue)
data.save_missed_states(guesed_states)

screen.exitonclick()

