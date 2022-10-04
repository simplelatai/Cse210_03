from game.terminal_service import TerminalService

class Jumper:
    """The Jumper class
    Attributes:
        self.draw : draw itself 
        self.remove : remove piece of itself if guess wrong
        self.check : check if any parachute left
        self.if no more parachute: if no draw x instead of o
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:    
        """
        self._jumper = [
             '__',
            '/  \\',
            '_____',
           '\     /',
           '\     /',
              'o',
             '/|\\',
             '/|\\',
            '^^^^^',

        ]
    
    def diplay_jumper(self):
        """Display the parachute on terminal"""
        for i in self._jumper:
            print(i)
    
    def has_parachute(self):
        """Change the number of lives player has"""
        return len(self._jumper) >= 5

    
    def remove_parachute(self):
        """Remover parachute one at a time"""
        self._jumper.pop(0)

    
    def draw_x(self): [
        last_letter =
            'x',
           '/|\\',
           '/ \\',
    
    ]
        for i in last_letter:
            print(i)   

    

    