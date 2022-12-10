from constants import *
from game.scripting.action import Action

class Counter(Action):
    
    def __init__(self):
        self.counter = 0

    def execute(self, cast, script, callback):
        self.counter += 1
        return self.counter

    def get_counter(self):
        return self.counter