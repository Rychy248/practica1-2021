import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

index = 0
for letter, word in phonetic_dict.items():
    if index >= 5:
        print("\n")
        index = 0
    print(letter," : ",word,end=" ")
    index += 1
print("\n")

def enter_word():
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please")
        enter_word()
    else:
        print("\n")
        for index in range(len(word)):
            print(word[index]," : ",output_list[index])
        print("\nHave a nice Day! :)")

enter_word()

