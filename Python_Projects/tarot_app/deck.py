import random


class TarotDeck:
    def major_arcana() -> list:
        # There are 22 major arcana cards
        # Start at 0 end at 21
        my_range = list(range(22))
        # intialize card values
        name_list = [
            "The Fool", 
            "The Magicican",
            "The High Priestess",
            "The Empress",
            "The Emperor",
            "The Hierophant",
            "The Lovers",
            "The Chariot",
            "Strength",
            "The Hermit",
            "Wheel of Fortune",
            "Justice",
            "The Hanged Man",
            "Death",
            "Temperance",
            "The Devil",
            "The Tower",
            "The Star",
            "The Moon",
            "The Sun",
            "Judgement",
            "The World"
        ]
        is_minor = False
        card_list = [
            [number, name, random.choice(["Upright", "Reversed"]), is_minor, img_index] for [number, name, img_index] in zip(my_range, name_list, my_range)
        ]
        return card_list

    def minor_arcana() -> list:
        my_range = list(range(2, 11))
        card_numbers = ["Ace"] + my_range + ["Page", "Knight", "Queen", "King"]
        suit_names = ["Wands", "Cups", "Swords", "Pentacles"]
        is_minor = True
        card_list = []

        def get_img(suit) -> int:
            img_index = 0
            match suit:
                case "Wands":
                    img_index += 21
                case "Cups":
                    img_index += 35
                case "Swords":
                    img_index += 49
                case "Pentacles":
                    img_index += 63
            return img_index

        # Because the lists are not the same length, we cannot use .zip
        for name in suit_names:
            img_index = get_img(name)
            for number in card_numbers:
                img_index += 1
                card = [number, name, random.choice(["Upright", "Reversed"]), is_minor, img_index]
                card_list.append(card)
        return card_list

    deck = major_arcana() + minor_arcana()
    random.shuffle(deck)
