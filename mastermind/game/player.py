class Player:
    """A person taking part in a game. The responsibility of Player is to keep track of their identity and last guess.
    
    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
        _guess (guess): The player's last guess.
    """
    
    def __init__(self, name, guess):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self._name = name
        self._guess = guess
        self._length = self._guess.get_number()
        self._status = self.create_asterisks()
        self._original_status = self.create_asterisks()
        
    def get_guess(self):
        """Returns the player's last guess (an instance of guess). If the player 
        hasn't guessd yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._guess

    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name

    def get_status(self):
        """Returns the player's game status.

        Args:
            self (Player): an instance of Player.
        """
        return self._status

    def set_guess(self, guess):
        """Sets the player's last guess to the given instance of guess.

        Args:
            guess (guess): an instance of guess
        """
        self._guess = guess
        
    def set_name(self, name):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        self._name = name

    def set_status(self, status):
        """Sets the player's last guess to the given instance of guess.

        Args:
            guess (guess): an instance of guess
        """
        self._status = status

    def create_asterisks(self):
        """ Create the list of asterisks to give the hint
        
            Args:
                self (Player): an instance of player
        """
        list_ast = [] 
        for i in range(self._length):
            list_ast.append('*')

        return list_ast
    
    def original_status(self):
        """ Return the hint to the original status
        
        Args:
            self (Player): an instance of Player

        """
        return self._original_status
