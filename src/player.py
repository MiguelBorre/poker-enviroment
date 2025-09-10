from card import Card

class Player:
    def __init__(self) -> None:
        self.hand = list[Card]
        self.active = True
        self.bet_pot = 0

    def fold(self):
        self.active = False

    def bet(self, bet: int):
        self.bet_pot += bet

    def check(self):
        pass

    def check_hand(self):
        pass

    def recive_card(self, card: Card) -> None:
        self.hand.append(card) #type: ignore
