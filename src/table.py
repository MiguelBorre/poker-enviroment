from deck import Deck

class Table:
    def __init__(self, big_blind: int, small_blind: int) -> None:
        self.community_cards = []
        self.pot = 0

        self.big_blind = big_blind
        self.small_blind = small_blind

    def add_comunity_card(self, deck: Deck):
        if len(self.community_cards) == 0: #type: ignore
            self.community_cards.append(deck.pop()) #type: ignore
            self.community_cards.append(deck.pop()) #type: ignore
            self.community_cards.append(deck.pop()) #type: ignore

        else:
            self.community_cards.append(deck.pop()) #type: ignore

    