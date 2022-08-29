import random
from deck import Deck

# Initialize a list of ints 
# Representing Major Arcana
def main():
    deck = Deck.deck
    random.shuffle(deck)
    def draw_card(deck):
        # Remove selection from list 
        # .pop returns removed element
        return deck.pop(0)

    def three_card_draw():
        my_list = ["past", "present", "future"]
        for item in my_list:
            print(f"Your {item}: {draw_card(deck)}")


    def eight_card_draw():
        my_list = ["identifier", "past", "present", "future", "best path", "environment", "hopes & fears", "ultimate outcome"]
        for item in my_list:
            print(f"Your {item}: {draw_card(deck)}")

    three_card_draw()
    print("\n")
    eight_card_draw()

if __name__ == "__main__":
    main()