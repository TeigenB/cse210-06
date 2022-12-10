from constants import *
from game.scripting.action import Action


class UserInput(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

        
    def execute(self, cast, script, callback):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        for letter in alphabet:
            if self._keyboard_service.is_key_pressed(letter): 
                cast.add_actor(input_GROUP, letter)
