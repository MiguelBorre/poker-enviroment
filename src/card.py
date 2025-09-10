class Card:
    def __init__(self, club: str, rank: int) -> None:
        self.club = club
        self.rank = rank

    def __str__(self) -> str:
        return f"{self.rank} of {self.club}" 
    

if __name__ == "__main__":
    carta = Card("spades", 1)

    print(carta)
