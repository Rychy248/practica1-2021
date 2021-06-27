def card_pack_f():
    card_pack ={ 
    "A": [11,1],
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
for pack_card in range(4):
        key_name = f"pack{pack_card}"
        cards[key_name] = card_pack_f()

card_pack_keys = []
for key in cards['pack3']:
    card_pack_keys.append(key)

print(card_pack_keys)
print(card_pack_keys[1])

print(cards)

poped = []
moment_dict = {}
moment_dict['A'] = cards['pack3'].pop('A')

poped.append(moment_dict)
print(poped)
print(cards)
