class Deck():

    def __init__(self):
        suits = ['♠', '♥', '♣', '♦']
        numbers = [
            {'number': 'A', 'value': 11},
            {'number': '2', 'value': 2},
            {'number': '3', 'value': 3},
            {'number': '4', 'value': 4},
            {'number': '5', 'value': 5},
            {'number': '6', 'value': 6},
            {'number': '7', 'value': 7},
            {'number': '8', 'value': 8},
            {'number': '9', 'value': 9},
            {'number': '10', 'value': 10},
            {'number': 'J', 'value': 10},
            {'number': 'Q', 'value': 10},
            {'number': 'K', 'value': 10},
        ]

        self.cards = []

        for suit in suits:
            for number in numbers:
                self.cards.append(Card(suit, number))

    def deal(self):
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)
