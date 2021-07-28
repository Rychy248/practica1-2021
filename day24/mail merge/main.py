"""
Hi! jorgeajrha@gmail.com
"""

"""
paths
input/letters
input/letters/starting_letter.txt
input/names/invited_names.txt
output/ready_to_send
main.py
"""

class AdminLetters():
    def __init__(self):
        self.names = []
        self.init_letter = ""
        self.read_names()
        self.read_letter()
        self.write_letters()
        
    def read_names(self):
        """Create a list of names"""
        with open("input/names/invited_names.txt") as file:
            self.names += file.readlines()
            index = 0
            for name in self.names:
                self.names[index] = name.strip()
                index += 1

    def read_letter(self):
        """Read the initial template of a letter"""
        with open("input/letters/starting_letter.txt") as file:
            self.init_letter += file.read()

    def write_letters(self):
        """Write the new letters"""
        #string.replace(oldvalue, newvalue, count) 
        for name in self.names:
            file_name = f"output/ready_to_send/letter_for_{name}.txt".lower()
            with open(file_name,"w") as file:
                file.write(self.init_letter.replace("[name]",f"{name}"))

writer = AdminLetters()
