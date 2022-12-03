from constants import *
from game.scripting.action import Action


class DrawArtifactAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        artifact = cast.get_first_actor(artifact_GROUP)
        body = artifact.get_body()   
        image = artifact.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)