import os
import time
import random

import day11_art as art


def c():
    if os.name in ['nt', 'dos']:
        command = "cls"
    else:
        command = "clear"
    os.system(command)


def clear():
    stay = input("Press enter to continue...")
    c()


# DAY END PROJECT
def init_cards_packs(pack_want=4):
    def card_pack_f():
        card_pack = {
            "A": [11, 1],
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "k": 10
        }
        return card_pack

    cards = {}
    for pack_card in range(pack_want):
        key_name = f"pack{pack_card}"
        cards[key_name] = card_pack_f()
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
            posible_sustract = [1, 5, 25, 50, 100, 500, 1000]

            print(f"\n Bank = ${player_bank}, beat = ${beat_var}")

            max_value = 0
            for value in posible_sustract:
                if value <= beat_var:
                    max_value = value

            options = 0
            value = 0
            while max_value >= posible_sustract[options] and options <= 6:
                value = posible_sustract[options]
                print(f"{options + 1} = -${value}")
                if options < 6:
                    options += 1
                else:
                    max_value = 0  # brek the while
            if options == 6 and value == 1000:
                options = 7

            option = int(input("8 or more = exit \nSelect a value for Sustract: "))
            if option <= 0:
                print("Invalid option!")
                time.sleep(2)
                c()
            elif option >= 8:
                if beat_var == 0:
                    print("Your beat can't be 0, we added one")
                    beat_var += 1
                    player_bank -= 1
                    print(f"Beat = ${beat_var}, Bank = ${player_bank}")
                    time.sleep(3)
                    c()
            elif option <= options:
                temp_beat_selected = posible_sustract[option - 1]
                beat_var -= temp_beat_selected
                player_bank += temp_beat_selected
                print(f"Less {temp_beat_selected}")
                if beat_var == 0:
                    print("\nIt's all your money,You're exiting... and...")
                    print("Your beat can't be 0, we added one")
                    beat_var += 1
                    player_bank -= 1
                    print(f"Beat = ${beat_var}, Bank = ${player_bank}")
                    option = options + 1
                    time.sleep(1)
                time.sleep(1)
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
            posible_adds = [1, 5, 25, 50, 100, 500, 1000]

            print(f"\n Bank = ${player_bank}, beat = ${beat_var}")

            max_value = 0
            for value in posible_adds:
                if value <= player_bank:
                    max_value = value

            options = 0
            value = 0
            while max_value >= posible_adds[options] and options <= 6:
                value = posible_adds[options]
                print(f"{options + 1} = +${value}")
                if options < 6:
                    options += 1
                else:
                    max_value = 0  # brek the while
            # Equilibrating options, to index of list posible_adds
            if options == 6 and value == 1000:
                options = 7

            option = int(input("8 or more = exit \nSelect a value for add: "))
            if option <= 0:
                print("Invalid option!")
                time.sleep(2)
                c()
            elif option >= 8:
                if beat_var == 0:
                    print("Your beat can't be 0, we added one")
                    beat_var += 1
                    player_bank -= 1
                    print(f"Beat = ${beat_var}, Bank = ${player_bank}")
                    time.sleep(2)
                    c()
            elif option <= options:
                temp_beat_selected = posible_adds[option - 1]
                beat_var += temp_beat_selected
                player_bank -= temp_beat_selected
                print(f"Added {temp_beat_selected}")
                if player_bank == 0:
                    print("It's all your money")
                    option = options + 1
                time.sleep(1)
                c()
            else:
                print("Option no reconcing")
                option = 0

    exit = False
    add_beat()
    while not exit:
        print(f"\nSTATE [Bank ${player_bank} | Beat ${beat_var}]")
        option = input("Press + to add in your beat, - for sustract, or 'Deal'!: ")
        option = option.lower()
        if option in "+ -":
            if option == '+':
                add_beat()
            else:
                sustract_beat()
        if option == "deal":
            exit = True
            print("Saving...")
            time.sleep(0.5)

    print(f"FINAL STATE [Bank ${player_bank} | Beat ${beat_var}]")
    time.sleep(1)
    c()

    return {'beat': beat_var, 'bank': player_bank}


def get_card(cards_a, player=0, dealer=0):
    cards_system = cards_a['cards']
    cards_player = cards_a['cards player']
    cards_dealer = cards_a['cards dealer']
    cards_stock = 0

    def stoc_card_f():
        nonlocal cards_stock
        nonlocal cards_system
        cards_stock = 0
        for key_pack in cards_system:
            cards_stock += len(cards_system[key_pack])

    stoc_card_f()

    def add_card_user(user_cards=[]):
        nonlocal cards_system
        nonlocal cards_stock
        cards_user = user_cards
        # selecting a deck
        card_pack_keys = []
        for key in cards_system:
            card_pack_keys.append(key)
        leght_pack = len(card_pack_keys)  # an index more
        random_pack = random.randint(1, leght_pack)
        random_pack -= 1  # substracting de extra index
        pack_key = card_pack_keys[random_pack]
        # selecting a card from deck selected
        card_keys = []
        for key in cards_system[pack_key]:
            card_keys.append(key)
        random_card = random.randint(0, len(card_keys) - 1)
        card_key = card_keys[random_card]
        # poping and adding de card
        moment_dict = {}
        moment_dict[card_key] = cards_system[pack_key].pop(card_key)
        cards_user.append(moment_dict)
        # cards_user[card_key] = cards_system[pack_key].pop(card_key)
        # delet if the dek is empty
        if len(cards_system[pack_key]) == 0:
            bum = cards_system.pop(pack_key)
        stoc_card_f()
        return cards_user

    while player > 0:
        cards_player = add_card_user(cards_player)
        player -= 1
    while dealer > 0:
        cards_dealer = add_card_user(cards_dealer)
        dealer -= 1

    # return
    all_cards = {
        'cards': cards_system,
        'cards player': cards_player,
        'cards dealer': cards_dealer,
        'cards stock': cards_stock
    }
    return all_cards


def get_score(cards_player=[], cards_dealer=[]):
    score_var = {
        'player': 0,
        'dealer': 0
    }
    a_in_player = 0
    a_in_dealer = 0

    for card in cards_player:  # score player
        for key in card:
            if key == 'A':  # two values
                score_var['player'] += 11
                a_in_player += 1
            else:
                score_var['player'] += int(card[key])
    for card in cards_dealer:  # socore system
        for key in card:
            if key == 'A':  # two values
                score_var['dealer'] += 11
                a_in_dealer += 1
            else:
                score_var['dealer'] += int(card[key])

    while score_var['player'] > 21 and a_in_player > 0:
        score_var['player'] -= 10
        a_in_player -= 1

    while score_var['dealer'] > 21 and a_in_dealer > 0:
        score_var['dealer'] -= 10
        a_in_dealer -= 1

    return score_var


def show_cards(cards_player, cards_dealer):
    height_player = len(cards_player)
    height_dealer = len(cards_dealer)

    print("Cards player <<[", end="")
    for card in cards_player:
        for key in card:
            print(key, end="")
        if height_player > 1:
            print(" - ", end="")
        height_player -= 1
    print("]>>")

    print("Cards dealer <<[", end="")
    for card in cards_dealer:
        for key in card:
            print(key, end="")
        if height_dealer > 1:
            print(" - ", end="")
        height_dealer -= 1
    print("]>>")


def continue_game(cards_a, beat_v, bank_v, score_v):
    cards = cards_a['cards']
    cards_stock = cards_a['cards stock']
    cards_player = cards_a['cards player']
    cards_dealer = cards_a['cards dealer']

    score = score_v
    beat = beat_v
    player_bank = bank_v

    def get_cards(player_n=0, dealer_n=0):
        nonlocal cards
        nonlocal cards_stock
        nonlocal cards_player
        nonlocal cards_dealer
        all_cards = {
            'cards': cards,
            'cards player': cards_player,
            'cards dealer': cards_dealer
        }
        moment_cards = get_card(all_cards, player_n, dealer_n)
        cards = moment_cards['cards']
        cards_stock = moment_cards['cards stock']
        cards_player = moment_cards['cards player']
        cards_dealer = moment_cards['cards dealer']

    def game_result(state='lose'):
        nonlocal beat
        nonlocal player_bank

        if state == 'win':
            player_bank += beat * 2
            print(f"You win ${beat * 2}")
        elif state == 'tie':
            player_bank += beat

        print(f"You lose ${beat}")
        beat = 0

    def show_hands():
        nonlocal score
        nonlocal cards_player
        nonlocal cards_dealer
        nonlocal player_bank
        nonlocal beat
        nonlocal cards_stock
        final_text = ""

        while score['dealer'] < 17:
            get_cards(player_n=0, dealer_n=1)
            score = get_score(cards_player, cards_dealer)
            c()
            art.logo_f(cards_player, player_bank, score, beat, first_dealer_card(), cards_stock)
            print("Dealer playing...")
            time.sleep(1)

        if score['player'] == score['dealer']:
            final_text = "Wow! You're tie"
            game_result('tie')
        elif score['player'] > 21:
            if score['dealer'] < score['player']:
                final_text = "sorry, you lose! :("
                game_result('lose')
            else:
                final_text = "congratulations, you win!"
                game_result('win')
        elif score['player'] <= 21:
            if score['dealer'] < score['player']:
                final_text = "congratulations, you win!"
                game_result('win')
            elif score['dealer'] <= 21:
                final_text = "Sorry, you lose! :("
                game_result('lose')
            elif score['dealer'] > 21:
                final_text = "congratulations, you win!"
                game_result('win')
        c()
        art.logo_f(cards_player, player_bank, score, beat, first_dealer_card(), cards_stock)
        print(final_text.upper(), "\n")
        print(f"Your score = {score['player']}, Dealer Total score = {score['dealer']}")
        show_cards(cards_player, cards_dealer)

    def first_dealer_card():
        nonlocal cards_dealer

        dealer_card = ''
        for key in cards_dealer[0]:
            dealer_card = key
        return dealer_card

    continue_g = True
    while continue_g:
        if beat == 0:  # continue whit cards from last game
            temp_beat_bank = select_beat(player_bank)
            player_bank = temp_beat_bank['bank']
            beat = temp_beat_bank['beat']
            get_cards(player_n=2, dealer_n=2)
            score = get_score(cards_player, cards_dealer)
            art.logo_f(cards_player, player_bank, score, beat, first_dealer_card(), cards_stock)

        skip_question = False
        if score['player'] == 21:
            if score['dealer'] == 21:
                print("Wow! You're tie")
                game_result('tie')
            else:
                print("Congratulations, You WIN!")
                game_result('win')
            print(f"Your score = {score['player']}, Dealer Total score = {score['dealer']}")
            show_cards(cards_player, cards_dealer)
            skip_question = True
        elif score['dealer'] == 21:
            print("Sorry, you lose! :(")
            print(f"Your score = {score['player']}, Dealer Total score = {score['dealer']}")
            game_result('lose')
            show_cards(cards_player, cards_dealer)
            skip_question = True

        if not skip_question and not beat * 2 > player_bank:
            print("Would you like to double the bet?")
            double_beat = input("Type yes = confirm or wathever = not: ")
            double_beat = double_beat.lower()
            if double_beat == 'yes':
                player_bank -= beat
                beat = beat * 2
                get_cards(player_n=1, dealer_n=0)
                score = get_score(cards_player, cards_dealer)
                print("Your card... ")
                time.sleep(1)
                show_hands()
                skip_question = True
        while not skip_question:
            print("Do you want a card more?")
            card_more = input("Type yes = confirm or wathever = show hands: ")
            card_more = card_more.lower()
            if card_more == 'yes':
                get_cards(player_n=1, dealer_n=0)
                score = get_score(cards_player, cards_dealer)
                c()
                art.logo_f(cards_player, player_bank, score, beat, first_dealer_card(), cards_stock)

                if score['player'] >= 21:
                    show_hands()
                    skip_question = True
            else:
                show_hands()
                skip_question = True

        if player_bank == 0 or cards_stock == 0:  # Sources are finished
            continue_g = False
        else:
            print("\nIf you want continue with your actual sources")
            want_continue = input("Type yes = confim, or wathever = no: ")
            want_continue = want_continue.lower()
            if want_continue == 'yes':
                continue_g = True
            else:
                continue_g = False
                # resetin cards
        cards_player = []
        cards_dealer = []

    print("Do you want A new Game?")
    try_option = input("Press yes, or no: ")
    try_option = try_option.lower()
    if try_option == 'yes':
        try_option = True
    else:
        try_option = False

    return try_option


def main():
    beat = 0
    cards = {}
    cards_stock = 1
    cards_player = []
    cards_dealer = []
    show_dealer_card = ''
    player_bank = 1000
    score = {
        'player': 0,
        'dealer': 0
    }

    cards = init_cards_packs(4)

    temp_beat_bank = select_beat(player_bank)
    player_bank = temp_beat_bank['bank']
    beat = temp_beat_bank['beat']

    all_cards = {
        'cards': cards,
        'cards player': cards_player,
        'cards dealer': cards_dealer
    }
    moment_cards = get_card(cards_a=all_cards, player=2, dealer=2)
    cards = moment_cards['cards']
    cards_stock = moment_cards['cards stock']
    cards_player = moment_cards['cards player']
    cards_dealer = moment_cards['cards dealer']

    score = get_score(cards_player, cards_dealer)
    dealer_card = ''
    for key in cards_dealer[0]:
        dealer_card = key

    art.logo_f(cards_player, player_bank, score, beat, dealer_card, cards_stock)

    try_again = continue_game(moment_cards, beat, player_bank, score)

    if try_again:
        main()


main()
