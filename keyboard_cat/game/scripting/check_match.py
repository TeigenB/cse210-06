from constants import *
from game.scripting.action import Action
from game.casting.cast import Cast
from game.services.keyboard_service import KeyboardService

class CheckMatch(Action):
    #this class will check if the user input is a match
    #with any of the existing artifacts.
    
    def __init__(self) -> None:
        self.castcast = Cast()
        self._keyboard_service = KeyboardService

    def check_match(self):
        enter = self._keyboard_service.is_key_down("enter")
        if enter:
             user_word = self.cast.get_actors(input_GROUP)
             game_words = self.cast.get_actors(artifact_GROUP)    
             for word in game_words:
                if user_word == word:
                      self._stats.add_points(1)