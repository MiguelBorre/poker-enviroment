from card import Card
from random import shuffle
from player import Player

class Deck:
    def __init__(self, n_decks: int) -> None:
        self.deck_card = list

        for _ in range(n_decks):
            for club in ["clubs", "spades", "diamonds", "heaths"]:
                for rank in range (1, 14):
                    self.deck_card.append(Card(club, rank)) # type: ignore

    def shuffle(self):
        shuffle(self.deck_card) #type: ignore

    def deal(self, players: list[Player]):
        for player in players:
            player.recive_card(self.pop())

    def pop(self) -> Card:
        return self.deck_card.pop(0) # type: ignore