from constants import *
from game.scripting.action import Action


class MoveArtifactAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        artifacts = cast.get_actors(artifact_GROUP)
        for artifact in artifacts:
            body = artifact.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)
