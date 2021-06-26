import os
import time
import day10_art as art

c = lambda : os.system('clear')

def clean():
    """
    Limpia la pantalla!
    """
    input("\n\nPress enter, to continue....")
    c()
 
 
#DAY END PROJECT

############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

def init_cards_packs():
        card_pack = [
            {"A": [11,1]},
            {"2": 2},
            {"3": 3},
            {"4": 4},
            {"5": 5},
            {"6": 6},
            {"7": 7},
            {"8": 8},
            {"9": 9},
            {"10": 10},
            {"J": 10},
            {"Q": 10},
            {"k": 10}
            ]

        cards = []
        for pack_card in range(4):
                cards.append(card_pack)
        return cards

def select_beat(bank=0):
        player_bank = bank
        beat_var = 0

        def sustract_beat():
                nonlocal player_bank
                nonlocal beat_var

                options = 7
                option = 0
                while option <= options: 
                        posible_sustract =[1,5,25,50,100,500,1000]

                        print(f"\n Bank = ${player_bank}, beat = ${beat_var}")

                        max_value = 0
                        for value in posible_sustract:
                                if value <= beat_var:
                                        max_value = value

                        options = 0
                        value = 0
                        while max_value >= posible_sustract[options] and options <= 6:
                                value = posible_sustract[options]
                                print(f"{options+1} = +${value}")
                                if options < 6:
                                        options+=1
                                else:
                                        max_value=0#brek the while
                        if options == 6 and value == 1000:
                                options = 7


                        option = int(input("8 or more = exit \nSelect a value for Sustract: "))
                        if option <= 0:
                                print("Invalid option!")
                                time.sleep(2)
                                c()
                        elif option >= 8:
                                if beat_var==0:
                                        print("Your beat can't be 0, we added one")
                                        beat_var += 1
                                        player_bank -= 1
                                        print(f"Beat = ${beat_var}, Bank = ${player_bank}")
                                        time.sleep(3)
                                        c()
                        elif option <= options:
                                temp_beat_selected = posible_sustract[option-1]
                                beat_var-= temp_beat_selected
                                player_bank+=temp_beat_selected 
                                print(f"Less {temp_beat_selected}")
                                if beat_var == 0:
                                        print("It's all your money,You're exiting... and...")
                                        print("Your beat can't be 0, we added one")
                                        beat_var += 1
                                        player_bank -= 1
                                        print(f"Beat = ${beat_var}, Bank = ${player_bank}")
                                        option = options +1
                                        time.sleep(3)
                                        c()
                        else:
                                print("Option no reconcing")
                                option = 0

       
        def add_beat():
                nonlocal player_bank
                nonlocal beat_var

                options = 7
                option = 0
                while option <= options: 
                        posible_adds =[1,5,25,50,100,500,1000]

                        print(f"\n Bank = ${player_bank}, beat = ${beat_var}")
                        
                        max_value = 0
                        for value in posible_adds:
                                if value <= player_bank:
                                        max_value = value

                        options = 0
                        value = 0
                        while max_value >= posible_adds[options] and options <= 6:
                                value = posible_adds[options]
                                print(f"{options+1} = +${value}")
                                if options < 6:
                                        options+=1
                                else:
                                        max_value = 0 #brek the while
                        #Equilibrating options, to index of list posible_adds
                        if options == 6 and value == 1000:
                                options = 7

                        option = int(input("8 or more = exit \nSelect a value for add: "))
                        if option <= 0:
                                print("Invalid option!")
                                time.sleep(2)
                                c()
                        elif option >= 8:
                                if beat_var==0:
                                        print("Your beat can't be 0, we added one")
                                        beat_var += 1
                                        player_bank -= 1
                                        print(f"Beat = ${beat_var}, Bank = ${player_bank}")
                                        time.sleep(3)
                                        c()
                        elif option <= options:
                                temp_beat_selected = posible_adds[option-1]
                                beat_var+= temp_beat_selected
                                player_bank-=temp_beat_selected 
                                print(f"Added {temp_beat_selected}")
                                if player_bank == 0:
                                        print("It's all your money")
                                        option = options +1
                                        time.sleep(3)
                                        c()
                        else:
                                print("Option no reconcing")
                                option = 0
        exit = False
        add_beat()
        while not exit:
                print(f"\nSTATE [Bank ${player_bank} | Beat ${beat_var}]")
                option = input("Press + to add in your beat, - for sustract, or 'Deal'! ")
                option = option.lower()
                if option in "+ -":
                        if option == '+':
                                add_beat()
                        else:
                                sustract_beat()
                if option == "deal":
                        exit = True
                        print("Saving...")
                        time.sleep(1)

        print(f"FINAL STATE [Bank ${player_bank} | Beat ${beat_var}]")
        time.sleep(2) 
        c()

        return {'beat':beat_var,'bank':player_bank}

def main():
        cards = []
        beat = 0
        cards_player = []
        cards_dealer = []
        show_dealer_card = ''
        player_bank = 1000
        score = {
                'player': 0,
                'dealer': 0
        }


        cards += init_cards_packs()
        temp_beat_bank = select_beat(player_bank)
        player_bank = temp_beat_bank['bank']
        beat = temp_beat_bank['beat']
        print(player_bank,beat,"Finished")

main()
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) 
#and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21
#remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21,
#then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card.
#If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the
#checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play.
#The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score.
#If the computer and user both have the same score, then it's a draw.
#If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0),
#then the user wins. If the user_score is over 21, then the user loses.
#If the computer_score is over 21, then the computer loses. If none of the above,
#then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game
#of blackjack and show the logo from art.py.








