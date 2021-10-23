import random


class Board:
    """The responsibility of Board is to keep track of the pieces in play.

    Attributes:
        board: A board is defined as a designated playing surface..
        
    """
    
    def __init__(self, length):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._secret_code = []
        self._length = length
        self._prepare()
        self.last_guess = ""   
        print(self._secret_code)   


    def apply(self, player):
        """
        Apply the changes to the board related to the guess of the player

        Args:
            self (Board): an instance of the board
            player (Player): the current player
        """
        self.last_guess = str(player.get_guess().get_number()) #do guess
        status = player.get_status()
        player.original_status()
        for num in range(self._length):
            if self.last_guess[num] == str(self._secret_code[num]):
                status[num] = 'x'
            elif status[num] == '*':
                result = self.last_guess.find(str(self._secret_code[num]))
                if result != -1:
                    status[num] = 'o'
        player.set_status(status)

        
    def is_answered(self):
        """ 
            Check if the guess is the same as the secret code

            Args:
                self(Board): an instance of the board
        """
        if self.last_guess == "".join(str(num) for num in self._secret_code):
            return True
        return False
        
        
    def to_string(self, roster):        
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """

        text = "\n--------------------"
        for player in roster.get_players():
            if len(str(player.get_guess().get_number())) == 1:
                text += (f"\nPlayer {player.get_name()}: {player.get_guess().create_dashes()}, ")
            else:
                text += (f"\nPlayer {player.get_name()}: {player.get_guess().get_number()}, ")
            for x in player.get_status():
                text += x
        text += "\n--------------------\n"

        return text
   
    def _prepare(self):
        """ 
        Prepares the board with the secret code
        Args:
           self (Board): an instance of Board.

        Returns:
            _secredt_code: a four digit number represented as a list with 4 items.
            The code is a randomly generated, four digit number between 1000 and 9999.

        """

        
        for i in range(self._length):
            if i == 0:
                self._secret_code.append(random.randint(1,9))
            else:
                self._secret_code.append(random.randint(0,9))
            

    