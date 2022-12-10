from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.body import Body


class DrawArtifactAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
    
    def execute(self, cast, script, callback):
        artifacts = cast.get_actors(artifact_GROUP)
        if artifacts == None:
                return
        for x in artifacts:
            body = x.get_body()   
            image = x.get_image()
            position = body.get_position()
            text = x.get_text()
            x.set_value(user_input_format.format(text))
            self._video_service.draw_image(image, position)
            self._video_service.draw_text(x, position, 1)