from constants import *
from game.scripting.action import Action

class GetText(Action):

    def __init__(self):
        pass

    def get_text(self):

        filename = "cse210-06/keyboard_cat/assets/data.txt"
        with open(filename, 'r') as file:
            list = file.readlines()
            text = random.choice(list)
            return text