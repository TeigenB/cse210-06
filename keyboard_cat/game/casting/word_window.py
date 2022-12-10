from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Word_Window(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, image, text = "", debug = False, align = ALIGN_DOWN, fontfile = FONT_FILE, size = FONT_LARGE):
        """Constructs a new word_window.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._align = align
        self._value = text
        self._fontfile = fontfile
        self._size = size

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_body(self):
        """Gets the word_window's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def align_down(self):

        return self._align
    
    def get_text(self):
        #gets the user entry
        #returns an instance of text

        return self._text
    
    def get_value(self):
        """Gets the text's value.
        
        Returns:
            A string containing the text's value.
        """

        return self._value

    def set_value(self, value):
        """Sets the text's value.
        
        Args:
            A string containing the text's value.
        """
        self._value = value
        return self._value

    def get_align(self):
            """Gets the alignment for the text.
            
            Returns:
                A number representing the text alignment.
            """
            return self._align

    def get_fontfile(self):
        """Gets the font file for the text.
        
        Returns:
            A string containing the font file.
        """
        return self._fontfile

    def get_size(self):
        """Gets the font size of the text.
        
        Returns:
            A number representing the font size.
        """
        return self._size

