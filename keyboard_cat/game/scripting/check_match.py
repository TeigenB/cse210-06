from constants import *
from game.scripting.action import Action
from game.casting.cast import Cast
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.casting.artifact import Artifact
from game.casting.body import Body
from game.casting.image import Image
from game.casting.text import Text

class CheckMatch(Action):
    #this class will check if the user input is a match
    #with any of the existing artifacts.
    
    def __init__(self) -> None:
        self._keyboard_service = RaylibKeyboardService()
        self._artifact = Artifact(Body, Image, Text)

    def execute(self, cast, script, callback):
        if self._keyboard_service.is_key_pressed(ENTER):
             user_letters = cast.get_actors(input_GROUP)
             user_word = ""

             for letter in user_letters:
                user_word += letter

             artifacts = cast.get_actors(artifact_GROUP)
             game_words = []    
             for artifact in artifacts:
                game_words.append(self._artifact.get_text())

             for word in game_words:
                if user_word == word:
                      self._stats.add_points(1)
