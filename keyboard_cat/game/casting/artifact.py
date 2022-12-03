from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Artifact(Actor):
    """A solid object that goes from the left side of the screen to the right side of the screen."""
    
    def __init__(self, body, image, text, debug = False):
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
