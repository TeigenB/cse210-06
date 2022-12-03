from constants import *
from game.scripting.action import Action
from game.casting.stats import Stats


class UserInput(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        self._stats = Stats
        
    def execute(self, cast):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
        for letter in alphabet:
            if self._keyboard_service.is_key_down(letter): 
                cast.add_actor(input_GROUP, letter)
