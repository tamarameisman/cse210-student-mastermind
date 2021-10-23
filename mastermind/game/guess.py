import random


class Guess:
    """The responsibility of Guess is to keep track of the hints in play.

    Attributes:
        board: A board is defined as a designated playing surface..
        
    """
    
    def __init__(self, name, user_guess):
        self._prepare()
        self._name = name
        self._user_guess = str(user_guess)
        self._hint = ["*","*","*","*"]

        

    def get_name(self):
        return self._name

    def get_number(self):
        return self._user_guess

    def get_hint(self, secret_code):

        right_number_right_postion = "x"
        right_number_only = "o"
        wrong = "*"
        right_place = 0
        for item in (self._user_guess):

            if int(item) == secret_code[right_place]:
                self._hint[right_place] = right_number_right_postion
            elif int(item) in secret_code:
                self._hint[right_place] = right_number_only
            else:
                self._hint[right_place] = wrong
            right_place += 1


                

        """if int(self._user_guess[0]) == secret_code[0]:
            self._hint[0] = right_number_right_postion
        
        elif secret_code[0] == int(self._user_guess[1]) or secret_code[0] == int(self._user_guess[2]) or secret_code[0] == int(self._user_guess[3]):
            self._hint[0] = right_number_only
            
        else:
            self._hint[0] = wrong

        if secret_code[1] == int(self._user_guess[1]):
            self._hint[1] = right_number_right_postion
        
        elif secret_code[1] == int(self._user_guess[0]) or secret_code[1] == int(self._user_guess[2]) or secret_code[1] == int(self._user_guess[3]):
            self._hint[1] = right_number_only
            
        else:
            self._hint[1] = wrong

        if secret_code[2] == int(self._user_guess[2]):
            self._hint[2] = right_number_right_postion
        
        elif secret_code[2] == int(self._user_guess[0]) or secret_code[2] == int(self._user_guess[1]) or secret_code[2] == int(self._user_guess[3]):
            self._hint[2] = right_number_only
            
        else:
            self._hint[2] = wrong

        if secret_code[3] == int(self._user_guess[3]):
            self._hint[3] = right_number_right_postion
        
        elif secret_code[3] == int(self._user_guess[0]) or secret_code[3] == int(self._user_guess[1]) or secret_code[3] == int(self._user_guess[2]):
            self._hint[3] = right_number_only
            
        else:
            self._hint[3] = wrong"""
        
        self._hint = random.shuffle(self._hint)
        return(f"{self._hint[0]}, {self._hint[1]}, {self._hint[2]}, {self._hint[3]}")

    
    def is_empty(self):
        pass
        
        
    '''def to_string(self):
        border = "--------------------"
        count = 0
        return f"" '''
   
    def _prepare(self):
        pass
    