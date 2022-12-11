from constants import *
from game.scripting.action import Action
from game.casting.cast import Cast
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.casting.artifact import Artifact
from game.casting.body import Body
from game.casting.image import Image
from game.casting.text import Text
from game.scripting.user_input import UserInput

class CheckMatch(Action):
    #this class will check if the user input is a match
    #with any of the existing artifacts.
    
    def __init__(self, stats) -> None:
        self._keyboard_service = RaylibKeyboardService()
        self._artifact = Artifact(Body, Image, Text)
        self.user_input = UserInput(self._keyboard_service)
        self._stats = stats

    def execute(self, cast, script, callback):
         user_letters = self.user_input.keys(cast)
         if user_letters:
            print(user_letters)


            user_word = "".join(user_letters)


            artifacts = cast.get_actors(artifact_GROUP) 
            for item in artifacts:
               if user_word == item.get_text():
                  self._stats.add_points(1)
                  cast.remove_actor(artifact_GROUP, item)
