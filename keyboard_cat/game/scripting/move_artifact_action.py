from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class MoveArtifactAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        artifacts = cast.get_actors(artifact_GROUP)
        if artifacts == None:
            return
        for artifact in artifacts:
            body = artifact.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            new_position = position.add(velocity)
            body.set_position(new_position)
