class Deck:
    def __init__(self):
        self.cards = ['A', 'K', 2, 5, 7]
    
    def __getItem__(self, key):
        return self.card[key]

    def __setItem__(self, key, val):
        self.cards[key] = val

    def __delItem__(self, key):
        del(self.cards[key])

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        return self.cards + other.cards

    def __repr__(self):
        return str(self.cards)

    def __str__(self):
        return str(self.cards)