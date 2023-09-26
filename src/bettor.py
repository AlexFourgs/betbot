"""Bettor class
"""

class Bettor:
    def __init__(self, discord_id: int, discord_name: str) -> None:
        self.id = discord_id
        self.name = discord_name

    def update_name(self, new_name: str) -> None:
        """Update the name in case it changes.

        While it is possible to change name on Discord, the id is still the same
        so this method allows to update the name.

        Parameters
        ----------
        new_name : str
            The new name.
        """
        self.name = new_name

    def __eq__(self, __value: object) -> bool:
        if self.id == __value.id:
            return True
        return False

    def __hash__(self) -> int:
        return hash((self.id))

    def __str__(self) -> str:
        return f'{self.name} ({self.id})\n'
