from flask import Flask, render_template
from deck import TarotDeck


def draw_card(deck):
    # Remove selection from list 
    # .pop returns removed element
    return deck.pop(0)

def three_card_draw():
    my_list = ["Past", "Present", "Future"]
    for item in my_list:
        card = draw_card(TarotDeck.deck)
        if card[3] == True:
            card[1] = f"of {card[1]}"
        yield (item, card[0], card[1], card[2], card[3], card[4])

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
        card = draw_card(TarotDeck.deck)
        if card[3] == True:
            card[1] = f"of {card[1]}"
        yield (item, card[0], card[1], card[2], card[3], card[4])

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/three")
def three_cards():
    return render_template("page.html", cards=three_card_draw())

@app.route("/eight")
def eight_cards():
    return render_template("page.html", cards=eight_card_draw())