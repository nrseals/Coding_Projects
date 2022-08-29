import random

class Deck:
    def major_arcana():
        # There are 22 major arcana cards
        # Start at 0 end at 21
        my_range = list(range(22))
        # intialize card values
        name_list = [
            "The Fool", "The Magicican", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers",
            "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower",
            "The Star", "The Moon", "The Sun", "Judgement", "The World"
            ]
        card_list = [(number, name, random.choice(["Upright", "Reversed"])) for [number, name] in zip(my_range, name_list)]
        return card_list

    def minor_arcana():
        my_range = list(range(2, 11))
        card_numbers = my_range + ["Page", "Knight", "Queen", "King" ,"Ace"]
        suit_names = ["Wands", "Cups", "Swords", "Pentacles"]
        card_list = []
        # Because the lists are not the same length, we cannot use .zip
        for name in suit_names:
            for number in card_numbers:
                card = (number, name, random.choice(["Upright", "Reversed"]))
                card_list.append(card)
        return card_list

    deck = major_arcana() + minor_arcana()