import gui
import random


class Card(gui.Sprite):
    def __init__(self, num: int, suit: str, face_up: list[bool]):
        self.num = num  # integer in range from 1 to 13
        self.suit = suit  # string containing the card's suit
        self.face_up = face_up  # defines which way the card is facing for each player

        # set the image path based on given number and suit
        self.num_str: str
        if 2 <= num <= 10:
            self.num_str = str(num)
        elif num == 1:
            self.num_str = "ace"
        else:
            royals = ["jack", "queen", "king"]
            self.num_str = royals[num - 11]

        self.up_img_path = f"Images/Cards/{self.num_str}_of_{self.suit}.png"
        self.down_img_path = f"Images/Cards/card_back.png"

    def __str__(self):
        return f"{self.num_str} of {self.suit}"

    def draw(self):
        super().draw()


class Deck(gui.Sprite):
    def __init__(self) -> object:
        self.cards: list[Card] = []  # list of cards in bottom-to-top order

    def add_card(self, card):
        self.cards.append(card)

    def add_deck(self, deck):
        self.cards.append(deck.cards[:])

    # removes and returns the top card from deck
    def take_top_card(self):
        if len(self.cards) > 0:
            top_card = self.cards[len(self.cards) - 1]
            self.cards.remove(top_card)

            return top_card
        else:
            return None

    def shuffle(self):
        random.shuffle(self.cards)


# global variables
sorted_deck: list[Card] = []  # constant set of all cards in sorted order
played_cards: list[Card] = []  # list of the two played cards
hand: list[Card] = []  # list of the active cards in each players' hand
draw: list[Deck] = []  # list of the two draw piles
side: list[Deck] = []  # list of the two side piles


def deal_cards():
    # define SORTED_DECK
    for n in range(1, 14):
        for s in ["clubs", "spades", "diamonds", "hearts"]:
            card = Card(n, s, [False, False])
            sorted_deck.append(card)

    # shuffle a dealing deck
    deal_deck = Deck()
    for c in sorted_deck:
        deal_deck.add_card(c)
    deal_deck.shuffle()

    # deal to each player
    for player in range(2):

        # deal to the hand
        for i in range(5):
            hand_card = deal_deck.take_top_card()
            hand_card.face_up[player] = True
            hand.append(hand_card)

        # deal to the draw pile
        for i in range(15):
            draw_deck = Deck()
            draw_deck.add_card(deal_deck.take_top_card())
            draw.append(draw_deck)

        # deal to the side pile
        for i in range(5):
            side_deck = Deck()
            side_deck.add_card(deal_deck.take_top_card())
            side.append(side_deck)

        # deal to the played card
        played_card = deal_deck.take_top_card()
        played_card.face_up = [True, True]
        played_cards.append(played_card)
