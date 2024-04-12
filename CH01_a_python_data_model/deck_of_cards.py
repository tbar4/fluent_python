import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# Card in deck
beer_card = Card("7", "diamonds")
print("Beer Card: ", beer_card)

# Initializing Deck
deck = FrenchDeck()
print("Length of Deck:", len(deck))

# Use getitem sttribute
print("Select card at index 0:", deck[0])
print("Select card at index 1:", deck[1])

# Get random card
print("Random Card:", choice(deck))

# __getitem__ allows for slicing and iteration
print("Get first 3 cards of deck:", deck[:3])
print("Get the 12 card and skip 13:", deck[12::13])

for card in deck:
    print("Card:", card)

for card in reversed(deck):
    print("Reversed Card:", card)

# __getitem__ also allows for `in` statements
print("Card Queen of Diamonds exists?", Card("Q", "diamonds") in deck)
print("Card T of None exists?", Card("T", "none") in deck)

# Sort the suits
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
