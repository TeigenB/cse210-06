from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        lives = cast.get_actors(LIVES_GROUP)
        if lives == 0:
            stats = cast.get_first_actor(STATS_GROUP)
            callback.on_next(GAME_OVER)