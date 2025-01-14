class Guess:
    """The responsibility of Board is to keep track of the pieces in play.

    Attributes:
        board: A board is defined as a designated playing surface..
        
    """
    
    def __init__(self, number):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        
        self._number = number

    def get_number(self):
        """Returns the number to remove from.

        Args:
            self (Guess): an instance of Guess.
        """
        return self._number
    
    def create_dashes(self):
        """
        Create dashes for the beginning of the game

        Args:
            self (Guess): an instance of the Guess
        """
        text = ''
        for i in range(self._number):
            text += '-'

        return text