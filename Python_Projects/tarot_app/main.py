from deck import TarotDeck



# Initialize a list of ints 
# Representing Major Arcana
def main():
    deck = TarotDeck.deck
    def draw_card(deck):
        # Remove selection from list 
        # .pop returns removed element
        return deck.pop(0)

    def three_card_draw():
        my_list = ["past", "present", "future"]
        for item in my_list:
            card = draw_card(deck)
            if card[3] == False:
                statement = f"{card[0]} {card[1]}, {card[2]}"
            else:
                statement = f"{card[0]} of {card[1]}, {card[2]}"
            yield (f"Your {item}: {statement}")


    def eight_card_draw():
        my_list = [
            "identifier", 
            "past", 
            "present", 
            "future", 
            "best path", 
            "environment", 
            "hopes & fears", 
            "ultimate outcome"
            ]
        for item in my_list:
            card = draw_card(deck)
            if card[3] == False:
                statement = f"{card[0]} {card[1]}, {card[2]}"
            else:
                statement = f"{card[0]} of {card[1]}, {card[2]}"
            yield (f"Your {item}: {statement}")

    for card in three_card_draw():
        print(card)
    print("\n")
    for card in eight_card_draw():
        print(card)


if __name__ == "__main__":
    main()