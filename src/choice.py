"""Choice class
"""

class NegativeNbBetException(Exception):
    """Raised when trying to remove bet with 0 nb_bet"""
    pass

class Choice:
    def __init__(self, choice: str, index: int, nb_bet: int = 0) -> None:
        self.choice = choice
        self.index = index
        self.nb_bet = nb_bet

    def bet_on(self) -> None:
        """Add a bet on current choice by incrementing the number of bet.
        """
        self.nb_bet += 1

    def remove_bet(self) -> None:
        """Remove a bet on current choice by decrementing the number of bet.

        Raises
        ------
        NegativeNbBetException
            Raised in case the number of bet is negative.
        """
        if self.nb_bet > 0:
            self.nb_bet -= 1
        else:
            # Real error here
            raise NegativeNbBetException

    def __eq__(self, __value: object) -> bool:
        if self.choice == __value.choice and \
            self.index == __value.index:
            return True
        return False

    def __str__(self) -> str:
        return f'{self.choice} ({self.nb_bet})'
