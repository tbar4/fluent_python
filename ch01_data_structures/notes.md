# The Python Data Model
The Python interpreter invokes special methods to perform basic object operations, often triggered by special syntax. The special method names are always written with leading and trailing double underscores. For example, the syntax obj[key] is supported by the \__getitem__ special method. In order to evaluate my_collection[key], the interpreter calls my_collection.\__getitem__(key).

## A Pythonic Card Deck

```python
import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])
```

The first thing to note is the use of collections.namedtuple to construct a simple class to represent individual cards. We use namedtuple to build classes of objects that are just bundles of attributes with no custom methods, like a database record.

```python
print(choice(deck))
```
We’ve just seen two advantages of using special methods to leverage the Python Data Model:

* Users of your classes don’t have to memorize arbitrary method names for standard operations. (“How to get the number of items? Is it .size(), .length(), or what?”)

* It’s easier to benefit from the rich Python standard library and avoid reinventing the wheel, like the random.choice function

```python
print(deck[:3])
print(deck[12:13])
```
Because our __getitem__ delegates to the [] operator of self._cards, our deck automatically supports slicing. It also makes it iterable.

```python
for card in deck:
    print(card)
```

Iteration is often implicit. If a collection has no __contains__ method, the in operator does a sequential scan. Case in point: in works with our FrenchDeck class because it is iterable.

```python
Card('Q', 'diamonds') in deck
Card('T', 'none') in deck
```

By implementing the special methods __len__ and __getitem__, our FrenchDeck behaves like a standard Python sequence, allowing it to benefit from core language features (e.g., iteration and slicing) and from the standard library, as shown by the examples using random.choice, reversed, and sorted. Thanks to composition, the __len__ and __getitem__ implementations can delegate all the work to a list object, self._cards.

```python
# Sort the suits
suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
```

## How Special Methods are Used