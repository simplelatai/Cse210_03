from game.terminal_service import TerminalService
import random

class Puzzle:

    """The secret word inside the Puzzle.
    
    The responsibility of a Puzzle, display a random word for player to guess.
    
    Attributes:
        word list: [].
        selected word: ""
        secret word : reveal secret word
    """

# 2) Create the class constructor. Use the following method comment.
    """Constructs a new Puzzle

        Args:
            self (Puzzle): An instance of Puzzle.
        """
    def __init__(self):
        self._word_list = ["kindness", "sun", "family"] 
        self._word_selected = ""
        self._select_word()
        self._word_guess = ["_ "] * len(self._word_selected)
        self._terminal_service = TerminalService()

# 3) Create the _selec-word(self) method. Use the following method comment.
    """Guess the letter .
        
        Returns:
            letter : word list,
        """
    """Randomly select from the word list"""
    def _select_word(self):
        self._word_selected = random.choice[self._word_list]
        
        
# 4) Create the draw_word_guess(self, location) method. Use the following method comment.
    """draw the word guess.

        Args:
            self (Puzzle): An instance of Puzzle.
    """
    def draw_word_guess(self):#director told us when it need to be drawn
        self._terminal_service.write_text(self._word_guess)

#5) create process_guess only you can do that
"""Need a parameter to tell it where to go"""
    
    def process_guess(self, guess_letter):
        counter = 0
        correctLetter = False
        for counter in range(len(self._word_selected)):
            if self._word_selected[counter] == guess_letter:
                self._word_guess[counter] == guess_letter + " "
                correctLetter = True
        return correctLetter
        
    
#6)Create can_keep_guessing 
"""The Puzzle will determine if the puzzle has been 
    solver or not"""
   
    def can_keep_guessing(self):
        if self._word_guess.find('_') == -1
            return False
        else
            return True