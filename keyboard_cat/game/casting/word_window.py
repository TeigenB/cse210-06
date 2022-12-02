from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Word_Window(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new word_window.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        #self._animation = animation

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    #def get_animation(self):
        """Gets the word_window's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the word_window's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

