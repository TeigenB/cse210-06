from constants import *
from game.casting.cast import Cast
from game.scripting.action import Action


class UserInput(Action):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, callback):
        #check = self._keyboard_service.is_key_pressed(any)
         pass    

    def keys(self, cast):
        if self._keyboard_service.is_key_pressed(ENTER):
            word = cast.get_actors(input_GROUP)
            cast.clear_actors(input_GROUP)
            return word
        else:
            for letter in self.alphabet:
                if self._keyboard_service.is_key_pressed(letter): 
                    cast.add_actor(input_GROUP, letter)
            return False
        
