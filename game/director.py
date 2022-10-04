from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        puzzle (Puzzle): The game's puzzle.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        
        self._is_playing = True
        self._word_selected = ""
        self.correctLetter = False
        self._puzzle = Puzzle()
        self._jumper = Jumper()
        self._terminal_service = TerminalService()

        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing == True
            self.draw_board()
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
    
    def draw_board(self):
        
        self._puzzle.draw_word_guess()#display
        self._jumper.display_parachute()
    
    def _get_inputs(self):
        """Get the input letter from user"""
        guess_letter = self._terminal_service.read_text("\nEnter a letter: ")
        
        
    def _do_updates(self):
        """Check if the user was correct and update"""
        self.correctLetter = self.puzzle.process_guest(self._word_select)
            if self.correctLetter == False
                self._jumper.remove_parachute()
                
            if self.correctLetter = self._puzzle.can_keep_guessing:
                if self._jumper.has_parachute
                    self.keep_palaying = True
                else:
                    self.keep_playing = False
                    self._jumper.draw_x()
                    sefl._jumper.draw_parachute()
        else:
            self.keep_playing = False
                
                
    def _do_outputs(self):
        if(self.correctLetter == True):
            print("You Win!")
        else:
            print("Try again!")
  