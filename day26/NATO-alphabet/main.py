import pandas

def words_phonetich(words):
    #word = words.replace(" ","")
    #phonetic_letters = {letter.upper():phonetic_dict[letter.upper()] for letter in word}
    phonetic_letters = [phonetic_dict[letter.upper()] for letter in word]
    return phonetic_letters

phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
#{new_key:new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter:row.code for index,row in phonetic_alphabet.iterrows()} 

typing = True
while typing:
    word = (input("Type a word: ").lower()).strip()
    if word == "exit":
        typing = False 
    else:
        index = 0
        for key_word in words_phonetich(word):
            print(word[index].upper()," = ",key_word)
            index+=1
