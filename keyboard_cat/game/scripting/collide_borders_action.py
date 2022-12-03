from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, audio_service):
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        artifact = cast.get_first_actor(artifact_GROUP)
        body = artifact.get_body()
        position = body.get_position()
        x = position.get_x()
        over_sound = Sound(OVER_SOUND)

    
        if x >= (FIELD_RIGHT):
            stats = cast.get_first_actor(STATS_GROUP)
            stats.lose_life()
            
            if stats.get_lives() == 0:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound) 

        cast.remove_actor(artifact_GROUP, artifact)