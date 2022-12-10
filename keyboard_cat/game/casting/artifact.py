from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Artifact(Actor):
    """A solid object that goes from the left side of the screen to the right side of the screen."""
    
    def __init__(self, body, image, text, debug = False, fontfile = FONT_FILE, size = FONT_LARGE, alignment = ALIGN_UP):
        """Constructs a new Artifact.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            text: the word that the user has to type 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._text = text
        self._value = text
        self._fontfile = fontfile
        self._size = size
        self._alignment = alignment

    def bounce_y(self):
        """pushes the artifact in the y direction."""
        velocity = self._body.get_velocity()
        x = velocity.get_x()
        y = velocity.get_y()
        velocity = Point(x, y)
        self._body.set_velocity(velocity)

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_body(self):
        """Gets the artifact's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the artifact's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_text(self):
        #gets the artifact's word
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
        return self._value

    def get_align(self):
            """Gets the alignment for the text.
            
            Returns:
                A number representing the text alignment.
            """
            return self._alignment

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

