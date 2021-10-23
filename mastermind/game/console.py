import random

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """
     
    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt, length):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            integer: The user's input as an integer.
        """
        user_input = 0
        while user_input == 0:
            test_numeric = False
            user_input =''
            while test_numeric == False or len(user_input) != length:
                user_input = input(prompt)
                test_numeric = user_input.isnumeric()
                if test_numeric == False or len(user_input) != length:
                    print(f"Please enter a number of {length} length long.")

            test_numeric = int(user_input)

            return test_numeric
        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)